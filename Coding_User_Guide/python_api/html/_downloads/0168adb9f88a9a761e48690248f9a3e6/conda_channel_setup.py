import sys
import os
import urllib.parse
import urllib.request
import json
import optparse

class CondaRepo():
    def __init__(self, py_version, is_win, is_linux, is_mac):
        self.py_version = py_version
        self.py_version_float = float(py_version)
        self.main_repos = ['https://repo.anaconda.com/pkgs/free/',
                           'https://repo.anaconda.com/pkgs/main/']
        self.output_path = ''
        self.is_win = is_win
        self.is_linux = is_linux
        self.is_mac = is_mac
        self.all_suffixes = ['noarch']

        if self.is_win:
            self.all_suffixes.append('win-64')
        if self.is_linux:
            self.all_suffixes.append('linux-64')
        if self.is_mac:
            self.all_suffixes.append('osx-64')
        
    
    @property
    def output_path(self):
        return self._output_path
    
    @output_path.setter
    def output_path(self, output_path):
        if not output_path:
            self._output_path = output_path
            return 
        
        if not os.path.isdir(output_path):
            raise OSError('channel path is not valid')
        if not os.access(output_path, os.W_OK):
            raise OSError('you do not have permission to write in the channel dir')
        self._output_path = output_path
    
    @property
    def py_version(self):
        return self._py_version
    
    @py_version.setter
    def py_version(self, py_version):
        if not py_version:
            self._py_version = py_version

        versions_dict = {'3.6' :'py36',
                         '3.7' :'py37',
                         '3.8' :'py38'
						 '3.9' :'py39',
						 '3.10':'py310',
						 '3.11':'py311'}
        self._py_version = versions_dict[py_version]
    
    @property
    def is_win(self):
        return self._is_win
    
    @is_win.setter
    def is_win(self, is_win):
        if type(is_win) == bool:
            self._is_win = is_win
            return

        bool_dict = {'true':True,
                     'false':False}
        self._is_win = bool_dict[is_win]
    
    @property
    def is_linux(self):
        return self._is_linux
    
    @is_linux.setter
    def is_linux(self, is_linux):
        if type(is_linux) == bool:
            self._is_linux = is_linux
            return

        bool_dict = {'true':True,
                     'false':False}
        self._is_linux = bool_dict[is_linux]
    
    @property
    def is_mac(self):
        return self._is_mac
    
    @is_mac.setter
    def is_mac(self, is_mac):
        if type(is_mac) == bool:
            self._is_mac = is_mac
            return

        bool_dict = {'true':True,
                     'false':False}
        self._is_mac = bool_dict[is_mac]

    def _create_subdir(self, subdir_name):
        dir_path = os.path.join(self.output_path, subdir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def _download_libs(self, repos_info, repo, repo_dir):
        subdir = repos_info['info']['subdir']
        subdir_tmp  = os.path.join(repo_dir,subdir)
        self._create_subdir(subdir_tmp)
        save_path = os.path.join(self.output_path, repo_dir, subdir)

        def perform_download(subdir, pack_name):
            pack_name = pack_name.replace('tar.bz2', 'conda')
            save_path_tmp = os.path.join(save_path, pack_name)
            if os.path.exists(save_path_tmp):
                return
            print('downloading : %s - %s ...'%(subdir, pack_name))
            try:
                down_path = os.path.join(repo, subdir, pack_name)
                req = urllib.request.Request(down_path)
                ret = urllib.request.urlopen(req)
            except:
                print('unable to download : %s - %s ...'%(subdir, pack_name))
                pack_name = pack_name.replace('conda', 'tar.bz2')
                save_path_tmp = os.path.join(save_path, pack_name)
                try:
                    print('downloading : %s - %s ...'%(subdir, pack_name))
                    down_path = os.path.join(repo, subdir, pack_name)
                    req = urllib.request.Request(down_path)
                    ret = urllib.request.urlopen(req)
                except:
                    print('unable to download : %s - %s ...'%(subdir, pack_name))
                    return

            with open(save_path_tmp, 'wb') as f:
                f.write(ret.read())
            ret.close()

        perform_download(subdir, 'repodata.json')
        perform_download(subdir, 'repodata.json.bz2')
        #perform_download(subdir, 'repodata_from_packages.json')
        
        for pack_name, pack_info in repos_info['packages'].items():
            if subdir == 'noarch':
                perform_download(subdir, pack_name)
            else:
                if 'py' not in pack_info['build'] or self.py_version in pack_info['build'] or 'py_0' in pack_info['build']:
                    perform_download(subdir, pack_name)

    def _get_repo_info(self, repo, suffix):
        repo_data_path = os.path.join(repo, suffix, 'repodata.json')        
        req = urllib.request.Request(repo_data_path)
        with urllib.request.urlopen(req) as response:
            data = json.load(response)
        return data
    
    def start_download(self):
        workers = []
        for repo in self.main_repos:
            if 'free' in repo:
                subdir = 'free'
            else:
                subdir = 'main'
            self._create_subdir(subdir)
            for suffix in self.all_suffixes:
                repos_info = self._get_repo_info(repo, suffix)
                self._download_libs(repos_info, repo, subdir)

def parse_options():
    parser = optparse.OptionParser()
    parser.add_option('-c','--channel-dir', action='store',
                    default='', dest='channel_dir',
                    help='the setup directory of the conda channel')
    parser.add_option('-w','--windows-download', action='store',
                    default='false', dest='win_down',
                    help='true or false to download windows libraries')
    parser.add_option('-l','--linux-download', action='store',
                    default='false', dest='linux_down',
                    help='true or false to download linux libraries')
    parser.add_option('-m','--mac-download', action='store',
                    default='false', dest='mac_down',
                    help='true or false to download mac libraries')
    parser.add_option('-p','--python-version', action='store',
                    default='3.3', dest='py_version',
                    help='The python version for which to seek libraries 3.x format')
    
    opts, args = parser.parse_args()

    return opts, args

def start():
    opts, args = parse_options()
    bool_str = ('true', 'false')
    py_versions = ('3.6', '3.7', '3.8', '3.9', '3.10', '3.11')
    if not opts.channel_dir.strip():
        print('Missing --channel-dir argument. Run --help for details')
        raise SystemExit(1)
    if opts.win_down.lower() not in bool_str:
        print('Incorrect --windows-download argument. Run --help for details')
        raise SystemExit(1)
    if opts.linux_down.lower() not in bool_str:
        print('Incorrect --linux-download argument. Run --help for details')
        raise SystemExit(1)
    if opts.mac_down.lower() not in bool_str:
        print('Incorrect --mac-download argument. Run --help for details')
        raise SystemExit(1)
    if opts.py_version.strip() not in py_versions:
        print('Incorrect --python-version argument. Run --help for details')
        raise SystemExit(1)
    
    cr_obj = CondaRepo(opts.py_version.strip(),
                       opts.win_down.lower(),
                       opts.linux_down.lower(),
                       opts.mac_down.lower())
    cr_obj.output_path = opts.channel_dir.strip()

    cr_obj.start_download()

start()
