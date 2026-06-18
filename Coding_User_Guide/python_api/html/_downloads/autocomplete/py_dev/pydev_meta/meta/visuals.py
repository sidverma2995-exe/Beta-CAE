from __future__ import annotations
from typing import Iterable, Callable, Any
import warnings
import typing_extensions
from . import annotations, boundaries, connections, coordsystems, elements, em, groups, isofunctions, materials, models, nodes, nvh, overlay, pages, parts, planes, plot2d, report, results, sections, spreadsheet, tdk, utils, visuals, vr, windows

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.get_center instead.")
def CenterOfImage(image_name: str, window_name: str) -> list[float]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.get_center` instead.


	This function gets the center (X,Y) of an image of a window with a given name. Center of image refers to the relative coordinates of the center point from the bottom left corner.

	Parameters
	----------
	image_name : str
		Name of the image.

	window_name : str
		Name of the window.

	Returns
	-------
	list[float]
		It returns a list where each member of the list is a float referring to the X and Y relative coordinates of the center point of the image from the bottom left corner.
		- [0] = X relative coordinate
		- [1] = Y relative coordinate
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    center = visuals.CenterOfImage(window_name, image_name)
		    if center:
		        xcent = center[0]
		        print(xcent)  # X center of image
		        ycent = center[1]
		        print(ycent)  # Y center of image
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.get_center instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_center instead.")
def CenterOfVideo(video_name: str, window_name: str) -> list[float]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_center` instead.


	This function gets the center (X,Y) of a video of a window with a given name. Center of video refers to the relative coordinates of the center point of the video from the bottom left corner.

	Parameters
	----------
	video_name : str
		Name of the video

	window_name : str
		Name of the window

	Returns
	-------
	list[float]
		It returns a list where each member of the list is a float referring to the X and Y relative coordinates of the center point of the video from the bottom left corner.
		- [0] = X relative coordinate
		- [1] = Y relative coordinate
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    center = visuals.CenterOfVideo(window_name, video_name)
		    if center:
		        xcent = center[0]
		        print(xcent)  # X center of video
		        ycent = center[1]
		        print(ycent)  # Y center of video
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_center instead.", DeprecationWarning)

def CollectNewImagesEnd() -> list[Image]:

	"""

	This function ends recording the creation of new images. This function should be preceded by a corresponding call to script function CollectNewImagesStart().

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image referring to one specific newly created image.
		Upon failure, an empty list is returned.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    visuals.CollectNewImagesStart()
		
		    # Create new images by importing new ones
		    utils.MetaCommand('image read image1 "/home/examples/pic2.jpg"')
		
		    new_images = visuals.CollectNewImagesEnd()
		    for img in new_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewImagesStart() -> int:

	"""

	This function starts recording the creation of new images. This function should be followed by a corresponding call to script function CollectNewImagesEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    visuals.CollectNewImagesStart()
		
		    # Create new images by importing new ones
		    utils.MetaCommand('image read image1 "/home/examples/pic2.jpg"')
		
		    new_images = visuals.CollectNewImagesEnd()
		    for img in new_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewVideosEnd() -> list[Video]:

	"""

	This function ends recording the creation of new videos. This function should be preceded by a corresponding call to script function CollectNewVideosStart().

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of class Video referring to one specific newly created video.
		Upon failure, an empty list is returned.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    visuals.CollectNewVideosStart()
		
		    # Create new videos by importing new ones
		    utils.MetaCommand('video read video1 "/home/examples/avi4.avi"')
		
		    new_videos = visuals.CollectNewVideosEnd()
		    for vid in new_videos:
		        print(
		            vid.name,
		            vid.window_name,
		            vid.width,
		            vid.height,
		            vid.filename,
		            vid.zorder,
		            vid.visible,
		            vid.page_id,
		            vid.frames,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def CollectNewVideosStart() -> int:

	"""

	This function starts recording the creation of new videos. This function should be followed by a corresponding call to script function CollectNewVideosEnd().

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    visuals.CollectNewVideosStart()
		
		    # Create new videos by importing new ones
		    utils.MetaCommand('video read video1 "/home/examples/avi4.avi"')
		
		    new_videos = visuals.CollectNewVideosEnd()
		    for vid in new_videos:
		        print(
		            vid.name,
		            vid.window_name,
		            vid.width,
		            vid.height,
		            vid.filename,
		            vid.zorder,
		            vid.visible,
		            vid.page_id,
		            vid.frames,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_current_frame instead.")
def CurrentFrameOfVideo(video_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_current_frame` instead.


	This function gets the number of the current frame of a video of a window with a given name.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns an integer referring to the number of the current frame of a video.
		Upon failure, it returns -1.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    current_frame = visuals.CurrentFrameOfVideo(window_name, video_name)
		    print(current_frame)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_current_frame instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_current_time instead.")
def CurrentTimeOfVideo(video_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_current_time` instead.


	This function gets the current time of a video of a window with a given name.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float referring to the current time of the video.
		Upon failure, it returns -1.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    current_time = visuals.CurrentTimeOfVideo(window_name, video_name)
		    print(current_time)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_current_time instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.delete instead.")
def DeleteImage(window_name: str, image_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.delete` instead.


	This function deletes an image of a window with a given name Window is specified by its name.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    ret = visuals.DeleteImage(window_name, image_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.delete instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.delete instead.")
def DeleteVideo(window_name: str, video_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.delete` instead.


	This function deletes a given video of a specified window.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    ret = visuals.DeleteVideo(window_name, video_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.delete instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.deselect instead.")
def DeselectImage(window_name: str, image_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.deselect` instead.


	This function deselects the image of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    ret = visuals.DeselectImage(window_name, image_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.deselect instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.deselect instead.")
def DeselectVideo(window_name: str, video_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.deselect` instead.


	This function deselects the video of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    ret = visuals.DeselectVideo(window_name, video_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.deselect instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_duration instead.")
def DurationOfVideo(video_name: str, window_name: str) -> float:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_duration` instead.


	This function gets the duration of a video of a window with a given name.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	float
		It returns a float referring to the duration of a video with a given name. 
		Upon failure, it returns -1.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    total_duration = visuals.DurationOfVideo(window_name, video_name)
		    print(total_duration)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_duration instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_frames instead.")
def FramesOfVideo(video_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_frames` instead.


	This function gets the number of frames of a video of a window with a given name.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns an integer referring to the number of frames of a video with a given name.
		Upon failure, it returns -1.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    total_frames = visuals.FramesOfVideo(window_name, video_name)
		    print(total_frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_frames instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.hide instead.")
def HideImage(window_name: str, image_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.hide` instead.


	This function hides the image of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    ret = visuals.HideImage(window_name, image_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.hide instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.hide instead.")
def HideVideo(window_name: str, video_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.hide` instead.


	This function hides the video of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    ret = visuals.HideVideo(window_name, video_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.hide instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.")
def Images() -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_images` instead.


	This function collects all images of all windows.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image referring to one specific image of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    all_images = visuals.Images()
		    for img in all_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.", DeprecationWarning)

def ImagesByName(image_name: str, window_name: str) -> list[Image]:

	"""

	This function finds images of a window with a given name.

	Parameters
	----------
	image_name : str
		Name of the image, a string expression for which wildcards can be used ("*", "?", "[...]").

	window_name : str
		Name of the window.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image referring to one specific image of the specified window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "*mag*"
		    name_images = visuals.ImagesByName(window_name, image_name)
		    for img in name_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def ImagesListToDict(images: str) -> dict:

	"""

	This function constructs a dictionary from a given list with Python objects of class Image.

	Parameters
	----------
	images : str
		List with Python objects of class Image.

	Returns
	-------
	dict
		It returns a dictionary whose key is the name of the image and value the corresponding Image object.
		Upon failure, an empty dictionary is returned.

	Notes
	-----
	If images with the same name exist in the given list, then only the first image will be saved in the dictionary.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    all_images = visuals.ImagesOfWindow(window_name)
		    if all_images:
		        dict_images = visuals.ImagesListToDict(all_images)
		        print(dict_images["image0"].filename)
		        for key, img in dict_images.items():
		            print(key, img.name, img.window_name)
		            print(img.width, img.height, img.filename, img.zorder)
		            print(img.visible, img.page_id)
		    else:
		        print("No image is loaded!")
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.")
def ImagesOfWindow(window_name: str) -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_images` instead.


	This function collects all images of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image referring to one specific image of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    window_images = visuals.ImagesOfWindow(window_name)
		    for img in window_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.", DeprecationWarning)

def IsImage(object: Any) -> int:

	"""

	This function checks whether a list object is of class Image.

	Parameters
	----------
	object : Any
		Any given object.

	Returns
	-------
	int
		It returns 1 if the list object is of type Image, or 0 if it is not.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    images = visuals.Images()
		    entities = list()
		    if len(images) > 0:
		        entities.append(images[0])
		    entities.append(None)
		
		    for ent in entities:
		        if visuals.IsImage(ent):
		            img = ent
		            print("This is an object of type image")
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		        else:
		            print("This is not an object of type image")
		
		
		if __name__ == "__main__":
		    main()


	"""

def IsVideo(object: Any) -> int:

	"""

	This function checks whether a list object is of class Video.

	Parameters
	----------
	object : Any
		Any given object.

	Returns
	-------
	int
		It returns 1 if the list object is of type Video, or 0 if it is not.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    videos = visuals.Videos()
		    entities = list()
		    if len(videos) > 0:
		        entities.append(videos[0])
		    entities.append(None)
		
		    for ent in entities:
		        if visuals.IsVideo(ent):
		            vid = ent
		            print("This is a struct of type video")
		            print(
		                vid.name,
		                vid.window_name,
		                vid.width,
		                vid.height,
		                vid.filename,
		                vid.zorder,
		                vid.visible,
		                vid.page_id,
		            )
		        else:
		            print("This is not an object of type video")
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadImage(filename: str, image_name: str, window_name: str) -> Image:

	"""

	This function loads an image on an existing window.

	Parameters
	----------
	filename : str
		Name of the file.

	image_name : str
		Name of the image.

	window_name : str
		Name of the window.

	Returns
	-------
	Image
		Upon success, it returns an object of class Image referring to the newly created image.
		Else, None is returned.

	Notes
	-----
	This function works for the active page.
	If there is an image with the given name then this function will fail.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image1"
		    filename = "/home/examples/pic2.jpg"
		    img = visuals.LoadImage(window_name, image_name, filename)
		    if img:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def LoadVideo(window_name: str, video_name: str, filename: str) -> Video:

	"""

	This function loads a video on an existing window.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	filename : str
		Name of the file.

	Returns
	-------
	Video
		Upon success, it returns an object of class Video referring to the newly created video.
		Else, a none is returned.

	Notes
	-----
	This function works for the active page.
	If there is a video with the given name then this function will fail.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video1"
		    filename = "/home/examples/avi5.avi"
		    vid = visuals.LoadVideo(window_name, video_name, filename)
		    if vid:
		        print(
		            vid.name,
		            vid.window_name,
		            vid.width,
		            vid.height,
		            vid.filename,
		            vid.zorder,
		            vid.visible,
		            vid.page_id,
		            vid.frames,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

def NamesOfAllImages(window_name: str) -> list[str]:

	"""

	This function get the names of all existing images of a window .

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[str]
		Upon success, it returns a listwhere each member of the list is a string referring to the name of an existing image of the specified window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    all_images = visuals.NamesOfAllImages(window_name)
		    for image_name in all_images:
		        print(image_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

def NamesOfAllVideos(window_name: str) -> list[str]:

	"""

	This function gets the names of all existing videos of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[str]
		Upon success, it returns a list where each member of the list is a string referring to the name of an existing video of the specified window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    all_videos = visuals.NamesOfAllVideos(window_name)
		    for video_name in all_videos:
		        print(video_name)
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.get_position instead.")
def PositionOfImage(image_name: str, window_name: str) -> list[float]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.get_position` instead.


	This function gets the position (X,Y) of an image of a window.

	Parameters
	----------
	image_name : str
		Name of the image.

	window_name : str
		Name of the window.

	Returns
	-------
	list[float]
		It returns a list where each member of the list is a float value referring to the X and Y relative coordinates of the image from the bottom left corner.
		- [0] = X relative coordinate
		- [1] = Y relative coordinate
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    position = visuals.PositionOfImage(window_name, image_name)
		    if position:
		        xpos = position[0]
		        print(xpos)  # X position of image
		        ypos = position[1]
		        print(ypos)  # Y position of image
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.get_position instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_position instead.")
def PositionOfVideo(video_name: str, window_name: str) -> list[float]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_position` instead.


	This function gets the position (X,Y) of a video of a window.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	list[float]
		It returns a list where each member of the list is a float referring to the X and Y relative coordinates of the video from the bottom left corner.
		- [0] = X relative coordinate
		- [1] = Y relative coordinate
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    position = visuals.PositionOfVideo(window_name, video_name)
		    if position:
		        xpos = position[0]
		        print(xpos)  # X position of video
		        ypos = position[1]
		        print(ypos)  # Y position of video
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_position instead.", DeprecationWarning)

def ReportNewImages() -> list[Image]:

	"""

	This function collects the newly created images from the last call of the script function CollectNewImagesStart(). This function should be preceded by a corresponding call to script function CollectNewImagesStart() and should be followed by a corresponding call to script function CollectNewImagesEnd().

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image referring to one specific newly created image.
		Upon failure, an empty list is returned.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    visuals.CollectNewImagesStart()  #  create new images
		    utils.MetaCommand('image read image10 "/home/examples/pic3.png"')
		
		    new_images = visuals.ReportNewImages()
		    for img in new_images:
		        print(img.name, img.window_name, img.width, img.height)
		        print(img.filename, img.zorder, img.visible, img.page_id)
		    visuals.CollectNewImagesEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

def ReportNewVideos() -> list[Video]:

	"""

	This function collects the newly created videos from the last call of script function CollectNewVideosStart(). This function should be preceded by a corresponding call to script function CollectNewVideosStart() and should be followed by a corresponding call to script function CollectNewVideosEnd().

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of type Video referring to one specific newly created video.
		Upon failure, an empty list is returned.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    visuals.CollectNewVideosStart()  # create new videos
		    utils.MetaCommand('video read video10 "/home/examples/avi4.avi"')
		
		    new_videos = visuals.ReportNewVideos()
		    for vid in new_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		    visuals.CollectNewVideosEnd()
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.get_scale instead.")
def ScaleOfImage(image_name: str, window_name: str) -> list[float]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.get_scale` instead.


	This function gets the scale factor (X,Y) of an image of a window. Scale factor refers to the original size of the image and it is a value greater than zero.

	Parameters
	----------
	image_name : str
		Name of the image.

	window_name : str
		Name of the window.

	Returns
	-------
	list[float]
		It returns a list where each member of the list is a float referring to the scale 
		factor of the image in X and Y direction.
		- [0] = X scale factor
		- [1] = Y scale factor
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    scale = visuals.ScaleOfImage(window_name, image_name)
		    if scale:
		        xscale = scale[0]
		        print(xscale)  # X scale factor of image
		        yscale = scale[1]
		        print(yscale)  # Y scale factor of image
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.get_scale instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_scale instead.")
def ScaleOfVideo(video_name: str, window_name: str) -> list[float]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_scale` instead.


	This function gets the scale factor (X,Y) of a video of a window. Scale factor refers to the original size of the video and it is a value greater than zero.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	list[float]
		It returns a list where each member of the list is a float referring to the scale factor of the video in X and Y direction.
		- [0] = X scale factor
		- [1] = Y scale factor
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    scale = visuals.ScaleOfVideo(window_name, video_name)
		    if scale:
		        xscale = scale[0]
		        print(xscale)  # X scale factor of video
		        yscale = scale[1]
		        print(yscale)  # Y scale factor of video
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_scale instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.select instead.")
def SelectImage(image_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.select` instead.


	This function selects the image of a window with a given name.

	Parameters
	----------
	image_name : str
		Name of the image.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    ret = visuals.SelectImage(window_name, image_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.select instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.select instead.")
def SelectVideo(video_name: str, window_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.select` instead.


	This function selects the video of a window with a given name.

	Parameters
	----------
	video_name : str
		Name of the video.

	window_name : str
		Name of the window.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    ret = visuals.SelectVideo(window_name, video_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.select instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.")
def SelectedImages() -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_images` instead.


	This function collects selected images of all windows.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of type Image referring to one specific selected image of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    selected_images = visuals.SelectedImages()
		    for img in selected_images:
		        print(img.name, img.window_name, img.width, img.height)
		        print(img.filename, img.zorder, img.visible, img.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.")
def SelectedImagesOfWindow(window_name: str) -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_images` instead.


	This function collects selected images of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of type Image referring to one specific selected image of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    selected_images = visuals.SelectedImagesOfWindow(window_name)
		    for img in selected_images:
		        print(img.name, img.window_name, img.width, img.height)
		        print(img.filename, img.zorder, img.visible, img.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_videos instead.")
def SelectedVideos() -> list[Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_videos` instead.


	This function collects selected videos of all windows.

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of type Video referring to one specific selected video of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    selected_videos = visuals.SelectedVideos()
		    for vid in selected_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height)
		        print(vid.filename, vid.zorder, vid.visible, vid.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_videos instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_videos instead.")
def SelectedVideosOfWindow(window_name: str) -> list[Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_videos` instead.


	This function collects selected videos of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of type Video referring to one specific selected video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    selected_videos = visuals.SelectedVideosOfWindow(window_name)
		    for vid in selected_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height)
		        print(vid.filename, vid.zorder, vid.visible, vid.page_id)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_videos instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.")
def SelectedVisuals() -> list[Image | Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_images` instead.


	This function collects selected visuals (images and videos) of all windows.

	Returns
	-------
	list[Image | Video]
		It returns a list wwhere each member of the list is an object of class Image or Video referring to one specific selected image or video of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image, meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    all_visuals = visuals.SelectedVisuals()
		    for vis in all_visuals:
		        if visuals.IsImage(vis):
		            img = vis
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		        elif visuals.IsVideo(vis):
		            vid = vis
		            print(
		                vid.name,
		                vid.window_name,
		                vid.width,
		                vid.height,
		                vid.filename,
		                vid.zorder,
		                vid.visible,
		                vid.page_id,
		                vid.frames,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.")
def SelectedVisualsOfWindow(window_name: str) -> list[Image | Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_images` instead.


	This function collects selected visuals (images and videos) of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Image | Video]
		It returns a list where each member of the list is an object of type Image or Video referring to one specific selected image or video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image, meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    selected_visuals = visuals.SelectedVisualsOfWindow(window_name)
		    for visual in selected_visuals:
		        if visuals.IsImage(visual):
		            img = visual
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		        elif visuals.IsVideo(visual):
		            vid = visual
		            print(
		                vid.name,
		                vid.window_name,
		                vid.width,
		                vid.height,
		                vid.filename,
		                vid.zorder,
		                vid.visible,
		                vid.page_id,
		                vid.frames,
		            )
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.set_center instead.")
def SetCenterOfImage(window_name: str, image_name: str, xcenter: float, ycenter: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.set_center` instead.


	This function sets the center (X,Y) of an image of a window with a given name. Center of image refers to the relative coordinates of the center point of the image from the bottom left cornerof the screen.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	xcenter : float
		The argument "xcenter" refers to the X position of the center point of the image.

	ycenter : float
		The argument "ycenter" refers to the Y position of the center point of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    xcenter = 0.19
		    ycenter = 0.21
		    ret = visuals.SetCenterOfImage(window_name, image_name, xcenter, ycenter)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.set_center instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.set_center instead.")
def SetCenterOfVideo(window_name: str, video_name: str, xcenter: float, ycenter: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.set_center` instead.


	This function sets the center (X,Y) of a video of a window with a given name. Center of video refers to the relative coordinates of the center point of the video from the bottom left corner.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	xcenter : float
		X center of the video.

	ycenter : float
		Y center of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    xcenter = 0.3
		    ycenter = 0.5
		    ret = visuals.SetCenterOfVideo(window_name, video_name, xcenter, ycenter)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.set_center instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.get_position instead.")
def SetPositionOfImage(window_name: str, image_name: str, xpos: float, ypos: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.get_position` instead.


	This function sets the position (X,Y) of an image of a window with a given name. Position of image refers to the relative coordinates of the image from the bottom left corner of the ssreen.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	xpos : float
		X position of the image.

	ypos : float
		Y position of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    xpos = 0.12
		    ypos = 0.09
		    ret = visuals.SetPositionOfImage(window_name, image_name, xpos, ypos)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.get_position instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.set_position instead.")
def SetPositionOfVideo(window_name: str, video_name: str, xpos: float, ypos: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.set_position` instead.


	This function sets the position (X,Y) of a video of a window with a given name. Position of video refers to the relative coordinates of the video from the bottom left corner of the screen.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	xpos : float
		X position of the video.

	ypos : float
		Y position of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    xpos = 0.19
		    ypos = 0.15
		    ret = visuals.SetPositionOfVideo(window_name, video_name, xpos, ypos)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.set_position instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.set_scale instead.")
def SetScaleOfImage(window_name: str, image_name: str, xscale: float, yscale: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.set_scale` instead.


	This function sets the scale factor (X,Y) of an image of a window. Scale factor refers to the original size of the image and it is a value greater than zero.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	xscale : float
		X scale factor of the image.

	yscale : float
		Y scale factor of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    xscale = 0.5
		    yscale = 0.6
		    ret = visuals.SetScaleOfImage(window_name, image_name, xscale, yscale)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.set_scale instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.set_scale instead.")
def SetScaleOfVideo(window_name: str, video_name: str, xscale: float, yscale: float) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.set_scale` instead.


	This function sets the scale factor (X,Y) of a video of a window. Scale factor refers to the original size of the video and it is a value greater than zero.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	xscale : float
		X scale factor of the video.

	yscale : float
		Y scale factor of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    xscale = 0.5
		    yscale = 0.6
		    ret = visuals.SetScaleOfVideo(window_name, video_name, xscale, yscale)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.set_scale instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.set_images_settings instead.")
def SetSettingsOfAllImages(window_name: str, image_settings: list[str]) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.set_images_settings` instead.


	This function controls settings of all images of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_settings : list[str]
		Argument 'image_settings' is a list which contains strings as members with the name and value of each setting separated by comma (e.g. 'align,bottom'). The names of the image settings and their possible values are:
		- 'align': Align Image to Window ('bottom', 'top', 'left', 'right', 'center')
		- 'align_hoffset': Horizontan offset (float)
		- 'align_voffset': Vertical offset (float)
		- 'autoscale': Scale with window resize (0,1)
		- 'filter': Image Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
		- 'filter_transparent': Transparency (integer)
		- 'pixel_aspect': Pixel Aspect ratio (float)
		- 'zorder': Z order (integer)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_settings = list()
		    image_settings.append("filter,blue")
		    image_settings.append("zorder,1")
		    ret = visuals.SetSettingsOfAllImages(window_name, image_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.set_images_settings instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.set_videos_settings instead.")
def SetSettingsOfAllVideos(window_name: str, video_settings: list[str]) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.set_videos_settings` instead.


	This function controls settings of all videos of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_settings : list[str]
		Argument 'video_settings' is a list which contains strings as members with the name and value of each setting separated by comma (e.g. 'options_width,6'). The names of the video settings and its possible values are:
		- 'align': Align Image to Window ('bottom', 'top', 'left', 'right', 'center')
		- 'align_hoffset': Horizontan offset (float)
		- 'align_voffset': Vertical offset (float)
		- 'autoscale': Scale with window resize (0,1)
		- 'filter': Image Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
		- 'filter_transparent': Transparency (integer)
		- 'swaprgb': Swap Video Colors (0,1)
		- 'pixel_aspect': Pixel Aspect ratio (float)
		- 'zorder': Z order (integer)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_settings = list()
		    video_settings.append("filter,blue")
		    video_settings.append("zorder,1")
		    ret = visuals.SetSettingsOfAllVideos(window_name, video_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.set_videos_settings instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.set_settings instead.")
def SetSettingsOfImage(window_name: str, image_name: str, image_settings: list[str]) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.set_settings` instead.


	This function controls settings of a given image of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	image_settings : list[str]
		Argument 'image_settings' is a list which contains strings as members with the name and value of each setting separated by comma (e.g. 'align,bottom'). The names of the image settings and their possible values are:
		- 'align': Align Image to Window ('bottom', 'top', 'left', 'right', 'center')
		- 'align_hoffset': Horizontan offset (float)
		- 'align_voffset': Vertical offset (float)
		- 'autoscale': Scale with window resize (0,1)
		- 'filter': Image Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
		- 'filter_transparent': Transparency (integer)
		- 'pixel_aspect': Pixel Aspect ratio (float)
		- 'zorder': Z order (integer)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image1"
		    image_settings = list()
		    image_settings.append("filter,blue")
		    image_settings.append("zorder,-3")
		    ret = visuals.SetSettingsOfImage(window_name, image_name, image_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.set_settings instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.set_settings instead.")
def SetSettingsOfVideo(window_name: str, video_name: str, video_settings: list[str]) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.set_settings` instead.


	This function controls settings of a given video specified of a given windows.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video

	video_settings : list[str]
		Argument 'video_settings' is a list which contains strings as members with the name and value of each setting separated by comma (e.g. 'options_width,6'). The names of the video settings and its possible values are:
		- 'align': Align Image to Window ('bottom', 'top', 'left', 'right', 'center')
		- 'align_hoffset': Horizontan offset (float)
		- 'align_voffset': Vertical offset (float)
		- 'autoscale': Scale with window resize (0,1)
		- 'filter': Image Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
		- 'filter_transparent': Transparency (integer)
		- 'swaprgb': Swap Video Colors (0,1)
		- 'pixel_aspect': Pixel Aspect ratio (float)
		- 'zorder': Z order (integer)

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    video_settings = list()
		    video_settings.append("filter,blue")
		    video_settings.append("zorder,-5")
		    ret = visuals.SetSettingsOfVideo(window_name, video_name, video_settings)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.set_settings instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.set_zorder instead.")
def SetZorderOfImage(window_name: str, image_name: str, zorder: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.set_zorder` instead.


	This function sets the zorder of an image of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	zorder : int
		Z-order of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    zorder = -5
		    ret = visuals.SetZorderOfImage(window_name, image_name, zorder)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.set_zorder instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.set_zorder instead.")
def SetZorderOfVideo(window_name: str, video_name: str, zorder: int) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.set_zorder` instead.


	This function sets the zorder of a video of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	zorder : int
		Z-order of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    zorder = -3
		    ret = visuals.SetZorderOfVideo(window_name, video_name, zorder)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.set_zorder instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.show instead.")
def ShowImage(window_name: str, image_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.show` instead.


	This function makes visible the image of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	image_name : str
		Name of the image.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image0"
		    ret = visuals.ShowImage(window_name, image_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.show instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.show instead.")
def ShowVideo(window_name: str, video_name: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.show` instead.


	This function makes visible the video of a window with a given name.

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video.

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Notes
	-----
	This function works for the active page.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "video0"
		    ret = visuals.ShowVideo(window_name, video_name)
		    print(ret)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.show instead.", DeprecationWarning)

def UpdateImage(image: Image) -> Image:

	"""

	This function updates the data of the given image object. Update is based on the fields 'name' and 'window_name' of the given image object.

	Parameters
	----------
	image : Image
		Object of class Image that refers to the updated image.

	Returns
	-------
	Image
		Upon success, it returns the new updated image object.
		Else, None is returned.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    window_name = "MetaPost"
		    image_name = "image*"
		    collected_images = visuals.ImagesByName(window_name, image_name)
		    for img in collected_images:
		        utils.MetaCommand("image hide " + img.name)  # commands to alter the image data
		        img = visuals.UpdateImage(img)
		        if img:  # Update OK
		            print(img.name, img.window_name, img.width, img.height, img.filename)
		            print(img.zorder, img.visible, img.page_id)
		        else:  # Update FAILED
		            print("This is not a valid image object")
		
		
		if __name__ == "__main__":
		    main()


	"""

def UpdateVideo(video: Video) -> Video:

	"""

	This function updates the data of the given video object. Update is based on the fields 'name' and 'window_name' of the given video object.

	Parameters
	----------
	video : Video
		Object of class Video.

	Returns
	-------
	Video
		Upon success, it returns the updated video object.
		Else, None is returned.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "*video*"
		    collected_videos = visuals.VideosByName(window_name, video_name)
		    for vid in collected_videos:
		        utils.MetaCommand("video hide " + vid.name)  # commands to alter the video data
		        vid = visuals.UpdateVideo(vid)
		        if vid:  # Update OK
		            print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		            print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		        else:  # Update FAILED
		            print("This is not a valid video object")
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_videos instead.")
def Videos() -> list[Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_videos` instead.


	This function collects all videos of all windows.

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of type Video referring to one specific video of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    all_videos = visuals.Videos()
		    for vid in all_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_videos instead.", DeprecationWarning)

def VideosByName(window_name: str, video_name: str) -> list[Video]:

	"""

	This function finds videos of a window with a given name (video_name).

	Parameters
	----------
	window_name : str
		Name of the window.

	video_name : str
		Name of the video. It is a string in which wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an onject of class Video referring to one specific video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		from meta import utils
		
		
		def main():
		    window_name = "MetaPost"
		    video_name = "*vid*"
		    name_videos = visuals.VideosByName(window_name, video_name)
		    for vid in name_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_videos instead.")
def VideosOfWindow(window_name: str) -> list[Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_videos` instead.


	This function collects all videos of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of class Video referring to one specific video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    window_videos = visuals.VideosOfWindow(window_name)
		    for vid in window_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_videos instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.")
def VisibleImages() -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_images` instead.


	This function collects visible images of all windows.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image referring to one specific visible image of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    visible_images = visuals.VisibleImages()
		    for img in visible_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.")
def VisibleImagesOfWindow(window_name: str) -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_images` instead.


	This function collects visible images of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class image referring to one specific visible image of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    visible_images = visuals.VisibleImagesOfWindow(window_name)
		    for img in visible_images:
		        print(
		            img.name,
		            img.window_name,
		            img.width,
		            img.height,
		            img.filename,
		            img.zorder,
		            img.visible,
		            img.page_id,
		        )
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_videos instead.")
def VisibleVideos() -> list[Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_videos` instead.


	This function collects visible videos of all windows.

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is a class of class Video referring to one specific visible video of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    visible_videos = visuals.VisibleVideos()
		    for vid in visible_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_videos instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_videos instead.")
def VisibleVideosOfWindow(window_name: str) -> list[Video]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_videos` instead.


	This function collects visible videos of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Video]
		It returns a list where each member of the list is an object of class video referring to one specific visible video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    visible_videos = visuals.VisibleVideosOfWindow(window_name)
		    for vid in visible_videos:
		        print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		        print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_videos instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.")
def VisibleVisuals() -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_images` instead.


	This function collects visible visuals (images and videos) of all windows.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image or Video referring to one specific visible image or video of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Video, meta.visuals.Image

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    visible_visuals = visuals.VisibleVisuals()
		    for visual in visible_visuals:
		        if visuals.IsImage(visual):
		            img = visual
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		        elif visuals.IsVideo(visual):
		            vid = visual
		            print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		            print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.")
def VisibleVisualsOfWindow(window_name: str) -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_images` instead.


	This function collects visible visuals (images and videos) of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image or Video referring to one specific visible image or video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image, meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    visible_visuals = visuals.VisibleVisualsOfWindow(window_name)
		    visible_visuals = visuals.Visuals()
		    for visual in visible_visuals:
		        if visuals.IsImage(visual):
		            img = visual
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		        elif visuals.IsVideo(visual):
		            vid = visual
		            print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		            print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.")
def Visuals() -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.pages.Page.get_images` instead.


	This function collects all visuals (images and videos) of all windows.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image or Video referring to one specific image or video of an existing window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image, meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    visible_visuals = visuals.Visuals()
		    for visual in visible_visuals:
		        if visuals.IsImage(visual):
		            img = visual
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		                img.page_id,
		            )
		        elif visuals.IsVideo(visual):
		            vid = visual
		            print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		            print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.pages.Page.get_images instead.", DeprecationWarning)

def VisualsByName(window_name: str, visual_name: str) -> list[Image]:

	"""

	This function finds visuals (images and videos) of a window.

	Parameters
	----------
	window_name : str
		Name of the window.

	visual_name : str
		A search string expression where wildcards can be used ("*", "?", "[...]").

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image or Video referring to one specific image or video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image, meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    visual_name = "video*"
		    name_visuals = visuals.VisualsByName(window_name, visual_name)
		    for ent in name_visuals:
		        if visuals.IsImage(ent):
		            img = ent
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		            )
		        elif visuals.IsVideo(ent):
		            vid = ent
		            print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		            print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.")
def VisualsOfWindow(window_name: str) -> list[Image]:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.windows.Window.get_images` instead.


	This function collects all visuals (images and videos) of a given window.

	Parameters
	----------
	window_name : str
		Name of the window.

	Returns
	-------
	list[Image]
		It returns a list where each member of the list is an object of class Image or Video referring to one specific image or video of the given window.
		Upon failure, an empty list is returned.

	Notes
	-----
	This function works for the active page.

	See Also
	--------
	meta.visuals.Image, meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    window_visuals = visuals.VisualsOfWindow(window_name)
		    for visual in window_visuals:
		        if visuals.IsImage(visual):
		            img = visual
		            print(
		                img.name,
		                img.window_name,
		                img.width,
		                img.height,
		                img.filename,
		                img.zorder,
		                img.visible,
		            )
		        elif visuals.IsVideo(visual):
		            vid = visual
		            print(vid.name, vid.window_name, vid.width, vid.height, vid.filename)
		            print(vid.zorder, vid.visible, vid.page_id, vid.frames)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.windows.Window.get_images instead.", DeprecationWarning)

def VideosListToDict(videos: str) -> dict:

	"""

	This function constructs a dictionary from a given list with python objects of class Video.

	Parameters
	----------
	videos : str
		List with Python objects of class Video.

	Returns
	-------
	dict
		It returns a dictionary whose key is the name of the video and value the corresponding Video object.
		Upon failure, an empty dictionary is returned.

	Notes
	-----
	If videos with the same name exist in the given list, then only the first video will be saved in the dictionary.

	See Also
	--------
	meta.visuals.Video

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    all_videos = visuals.VideosOfWindow(window_name)
		    print(all_videos)
		
		    if all_videos:
		        dict_videos = visuals.VideosListToDict(all_videos)
		        print(dict_videos)
		        for key, vid in dict_videos.items():
		            print(key, vid.name, vid.window_name)
		            print(vid.width, vid.height, vid.filename, vid.zorder)
		            print(vid.visible, vid.page_id, vid.frames)
		    else:
		        print("No video is loaded!")
		
		
		if __name__ == "__main__":
		    main()


	"""

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_attributes instead.")
def AttributesOfVideo(window_name: str, video_name: str) -> list:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_attributes` instead.


	This function collects all attributes of a given video

	Parameters
	----------
	window_name : str
		The name of the window

	video_name : str
		The name of the video

	Returns
	-------
	list
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    media_name = "video0"
		    all_attributes = visuals.AttributesOfVideo(window_name, media_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_attributes instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.get_attributes instead.")
def AttributesOfImage(window_name: str, image_name: str) -> list:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.get_attributes` instead.


	This function collects all attributes of a given image

	Parameters
	----------
	window_name : str
		The name of the window

	image_name : str
		The name of the image

	Returns
	-------
	list
		It returns a list where each member of the list is another list referring to one specific attribute of the given curve.
		In position 0, internal lists contain a string referring to the name of the attribute.
		In position 1, internal lists contain a string referring to the value of the attributes.
		Upon failure, an empty list is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    media_name = "image0"
		    all_attributes = visuals.AttributesOfImage(window_name, media_name)
		    for attr in all_attributes:
		        attrib_name = attr[0]
		        attrib_value = attr[1]
		        print("Name: " + attrib_name + "\\tValue: " + attrib_value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.get_attributes instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.get_attributes instead.")
def AttributeOfVideo(window_name: str, video_name: str, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	video_name : str
		The name of the video

	attrib_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    media_name = "video0"
		    name = "Z-order"
		
		    value = visuals.AttributeOfVideo(window_name, media_name, name)
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.get_attributes instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.get_attributes instead.")
def AttributeOfImage(window_name: str, image_name: str, attrib_name: str) -> str:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.get_attributes` instead.


	This function returns the value of a specific attribute.

	Parameters
	----------
	window_name : str
		The name of the window

	image_name : str
		The name of the image

	attrib_name : str
		Name of the attribute

	Returns
	-------
	str
		Upon success, it returns a string with the value of the given argument.
		Else, an empty string is returned.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    media_name = "image0"
		    name = "Z-order"
		
		    value = visuals.AttributeOfImage(window_name, media_name, name)
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.get_attributes instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Video.set_attribute instead.")
def SetAttributeOfVideo(window_name: str, video_name: str, attrib_name: str, attrib_value: str | float, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Video.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given model. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	video_name : str
		The name of the video.

	attrib_name : str
		Name of the attribute.

	attrib_value : str | float
		Value of the attribute. It can be either a number or a string.

	attribute_type : str
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    media_name = "video0"
		
		    name = "attr"
		    val = "val"
		    value = visuals.SetAttributeOfVideo(window_name, media_name, name, val)
		    print(value)
		    # or
		    name = "num_attr"
		    val = 10.1
		    attribute_type = "numerical"
		    value = visuals.SetAttributeOfVideo(
		        window_name, media_name, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Video.set_attribute instead.", DeprecationWarning)

@typing_extensions.deprecated("Deprecated since version 20.1.0.Use meta.visuals.Image.set_attribute instead.")
def SetAttributeOfImage(window_name: str, image_name: str, attribute_name: str, attribute_value: str | float, attribute_type: str) -> int:

	"""
	.. deprecated:: 20.1.0
		Use :py:meth:`meta.visuals.Image.set_attribute` instead.


	This function sets the value of a specific User Specified attribute referring to a given model. If the given attribute does not exist it is automatically created and its value is set.

	Parameters
	----------
	window_name : str
		The name of the window.

	image_name : str
		The name of the image.

	attribute_name : str
		Name of the attribute.

	attribute_value : str | float
		Value of the attribute. It can be either a number or a string.

	attribute_type : str
		Type of the attribute. Accepted values are "numerical" for numerical attributes or "string" for string attributes. Default value is "string".

	Returns
	-------
	int
		It returns 1 upon success and 0 upon failure.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    window_name = "MetaPost"
		    media_name = "image0"
		
		    name = "attr"
		    val = "val"
		    value = visuals.SetAttributeOfImage(window_name, media_name, name, val)
		    print(value)
		    # or
		    name = "num_attr"
		    val = 123
		    attribute_type = "numerical"
		    value = visuals.SetAttributeOfImage(
		        window_name, media_name, name, val, attribute_type
		    )
		    print(value)
		
		
		if __name__ == "__main__":
		    main()


	"""

	warnings.warn("Deprecated since version 20.1.0.Use meta.visuals.Image.set_attribute instead.", DeprecationWarning)

class Image():

	"""

	A class to describe images.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
		    print(img)
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the image.

	"""

	window_name: str = None
	"""
	Name of the window of the image.

	"""

	width: int = None
	"""
	Width of the image.

	"""

	height: int = None
	"""
	Height of the image.

	"""

	filename: str = None
	"""
	Filename of the image.

	"""

	zorder: int = None
	"""
	Z-order of the image.

	"""

	visible: int = None
	"""
	- 1 if image is visible
	- 0 if it is not visible

	"""

	page_id: int = None
	"""
	Id of the page of the image.

	"""

	def get_window(self) -> windows.Window:

		"""

		This methods gets the window of the image.


		Returns
		-------
		windows.Window
			Upon success, it returns an object of type Window referring to the window of the image. Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    win = img.get_window()
			    print(win)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_page(self) -> pages.Page:

		"""

		This method gets the page of the image.


		Returns
		-------
		pages.Page
			Upon success, it returns an object of type Page referring to the page of the image. Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    pag = img.get_page()
			    print(pag)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_position(self) -> list[float]:

		"""

		This method gets the position (X,Y) of the image.


		Returns
		-------
		list[float]
			Upon success, it returns a list where each member of the list is a float value referring to the X and Y relative coordinates of the image from the bottom left corner.- [0] = X relative coordinate- [1] = Y relative coordinateUpon failure, an empty list is returned.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    position = img.get_position()
			    print(position)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_scale(self) -> list[float]:

		"""

		This function gets the scale factor (X,Y) of the image. Scale factor refers to the original size of the image and it is a value greater than zero.


		Returns
		-------
		list[float]
			Upon success, it returns a list where each member of the list is a float referring to the scale factor of the image in X and Y direction.- [0] = X scale factor- [1] = Y scale factorUpon failure, an empty list is returned.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    scale = img.get_scale()
			    print(scale)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_center(self) -> list[float]:

		"""

		This function gets the center (X,Y) of the image. Center of image refers to the relative coordinates of the center point from the bottom left corner.


		Returns
		-------
		list[float]
			Upon success, it returns a list where each member of the list is a float referring to the X and Y relative coordinates of the center point of the image from the bottom left corner.- [0] = X relative coordinate- [1] = Y relative coordinateUpon failure, an empty list is returned.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    center = img.get_center()
			    print(center)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_attributes(self, attribute_name: str) -> dict:

		"""

		This method gets the attributes of the image.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute

		Returns
		-------
		dict
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    attribute_name = "width"
			    attr = img.get_attributes(attribute_name)
			    print(attr)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def delete(self) -> bool:

		"""

		This method deletes the image.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    ret = img.delete()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def show(self) -> bool:

		"""

		This method shows the image.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    ret = img.show()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def hide(self) -> bool:

		"""

		This method hides the image.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    ret = img.hide()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def select(self) -> bool:

		"""

		This method selects the image.


		Returns
		-------
		bool
			Upon sucess, it returns True. Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    ret = img.select()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def deselect(self) -> bool:

		"""

		This method deselects the image.


		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    ret = img.deselect()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_zorder(self, zorder: int) -> bool:

		"""

		This method sets the zorder of the image.


		Parameters
		----------
		zorder : int
			Z order of the image.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    zorder = 3
			    ret = img.set_zorder(zorder)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_position(self, position: List[float,float]) -> bool:

		"""

		This method sets the position (X,Y) of the image. Position of image refers to the relative coordinates of the image from the bottom left corner of the screen. This method works for the active page.


		Parameters
		----------
		position : list[float,float]
			Position of the image.
			A list with doubles: 
			[0]: X position
			[1]: Y position

		Returns
		-------
		bool
			Upon success, it returns True. Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    position = [0.5, 0.5]
			    ret = img.set_position(position)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_center(self, center: List[float,float]) -> bool:

		"""

		This method sets the center (X,Y) of the image. Center of image refers to the relative coordinates of the center point of the image from the bottom left cornerof the screen. This method works for the active page.


		Parameters
		----------
		center : list[float,float]
			Center of the image. 
			A list with doubles:
			[0]: X position
			[1]: Y position

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    center = [0.7, 0.3]
			    ret = img.set_center(center)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_scale(self, scale: List[float,float]) -> bool:

		"""

		This method sets the scale factor (X,Y) of the image. Scale factor refers to the original size of the image and it is a value greater than zero. This method works for the active page.


		Parameters
		----------
		scale : list[float,float]
			Scale factors of the image. 
			A list with doubles:
			[0]: X scale factor
			[1]: Y scale factor

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    scale = [0.2, 1.3]
			    ret = img.set_scale(scale)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_settings(self, settings: dict) -> bool:

		"""

		This method sets the settings of the image. This method works for the active page.


		Parameters
		----------
		settings : dict
			Settings (key-value) of the image.
			A dictionary with string keys and string values:
			 - 'align': Align Image to Window ('bottom', 'top', 'left', 'right', 'center')
			- 'align_hoffset': Horizontan offset (float)
			- 'align_voffset': Vertical offset (float)
			- 'autoscale': Scale with window resize (0,1)
			- 'filter': Image Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
			- 'filter_transparent': Transparency (integer)
			- 'pixel_aspect': Pixel Aspect ratio (float)
			- 'zorder': Z order (integer)

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    settings = {
			        "zorder": "2",
			        "align": "top",
			        "align_hoffset": 1.0,
			        "align_voffset": 1.0,
			        "autoscale": 0.2,
			        "filter": "red",
			        "filter_transparent": 20,
			        "pixel_aspect": 1.2,
			    }
			    ret = img.set_settings({settings})
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: str | float) -> bool:

		"""

		This method sets the value of a specific User Specified attribute of the image. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. 
			Its possible values are:
			'string': String
			'numerical': Number

		attribute_value : str | float
			Value of the attribute.
			Either a string, or a double depending on the attribute type.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    attribute_name = "extra"
			    attribute_type = "numerical"
			    attribute_value = 30
			    ret = img.set_attribute(attribute_name, attribute_type, attribute_value)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Image entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    img = visuals.Image(name="image1", window_name="MetaPost", page_id=0)
			    ret = img.is_usable()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def __init__(self, name: str, window_name: str, page_id: int) -> None:

		"""

		Upon success it returns an object of class Image for the given image name, window name and page id.


		Parameters
		----------
		name : str
			Name of the image.

		window_name : str
			Name of the window of the image.

		page_id : int
			Id of the page of the image.

		Returns
		-------
		None

		"""

class Video():

	"""

	Class for videos.

	Examples
	--------
	::

		# PYTHON script
		import meta
		from meta import visuals
		
		
		def main():
		    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
		    print(
		        vid.name,
		        vid.window_name,
		        vid.width,
		        vid.height,
		        vid.filename,
		        vid.zorder,
		        vid.visible,
		        vid.page_id,
		        vid.frames,
		    )
		
		
		if __name__ == "__main__":
		    main()

	"""


	name: str = None
	"""
	Name of the video.

	"""

	window_name: str = None
	"""
	Name of the window.

	"""

	width: int = None
	"""
	Width of the video.

	"""

	height: int = None
	"""
	Height of the video.

	"""

	filename: str = None
	"""
	Filename of the video.

	"""

	zorder: int = None
	"""
	Z-order of the video.

	"""

	visible: int = None
	"""
	- 1 if video is visible
	- 0 if it is not visible

	"""

	page_id: int = None
	"""
	Id of the page of the video.

	"""

	frames: int = None
	"""
	Number of video frames.

	"""

	def get_window(self) -> list[Video]:

		"""

		This method gets the window of the video.


		Returns
		-------
		list[Video]
			Upon success, it returns an object of type Video referring to the window of the video.Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    win = vid.get_window()
			    print(win)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_page(self) -> pages.Page:

		"""

		This method gets the page of the video.


		Returns
		-------
		pages.Page
			Upon success, it returns an object of type Page referring to the page of the image. Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    pag = vid.get_page()
			    print(pag)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_position(self) -> list[float]:

		"""

		This method gets the position (X,Y) of the video.


		Returns
		-------
		list[float]
			Upon success, it returns a list where each member of the list is a float referring to the X and Y relative coordinates of the video from the bottom left corner.- [0] = X relative coordinate- [1] = Y relative coordinateUpon failure, an empty list is returned.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    position = vid.get_position()
			    print(position)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_scale(self) -> list[float]:

		"""

		This method gets the scale factor (X,Y) of the video. Scale factor refers to the original size of the video and it is a value greater than zero.


		Returns
		-------
		list[float]
			Upon success, it returns a list where each member of the list is a float referring to the scale factor of the video in X and Y direction.- [0] = X scale factor- [1] = Y scale factorUpon failure, an empty list is returned.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    scale = vid.get_scale()
			    print(scale)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_center(self) -> list[float]:

		"""

		This method gets the center (X,Y) of the video. Center of video refers to the relative coordinates of the center point of the video from the bottom left corner.


		Returns
		-------
		list[float]
			Upon success, it returns a list where each member of the list is a float referring to the X and Y relative coordinates of the center point of the video from the bottom left corner.- [0] = X relative coordinate- [1] = Y relative coordinateUpon failure, an empty list is returned.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    center = vid.get_center()
			    print(center)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_frames(self) -> int:

		"""

		This method gets the number of frames of the video.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the number of frames of the video.Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    frames = vid.get_frames()
			    print(frames)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_current_frame(self) -> int:

		"""

		This method gets the number of the current frame of the video.


		Returns
		-------
		int
			Upon success, it returns an integer referring to the number of the current frame of the video.Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    current_frame = vid.get_current_frame()
			    print(current_frame)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_duration(self) -> float:

		"""

		This method gets the duration of the video.


		Returns
		-------
		float
			Upon success, it returns a float referring to the duration of the video. Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    duration = vid.get_duration()
			    print(duration)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_current_time(self) -> float:

		"""

		This method gets the current time of the video.


		Returns
		-------
		float
			Upon success, it returns a float referring to the current time of the video.Upon failure, it returns None.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    current_time = vid.get_current_time()
			    print(current_time)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def get_attributes(self, attribute_name: str) -> dict:

		"""

		This methods gets the attributes of the video.


		Parameters
		----------
		attribute_name : str, optional
			Name of the attribute.

		Returns
		-------
		dict
			Upon success, it returns a dictionary having as keys the name of the attributes as string and as values the value of the attributes. Upon failure, it returns an empty dictionary.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    attribute_name = "width"
			    attr = vid.get_attributes(attribute_name)
			    print(attr)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_zorder(self, zorder: int) -> bool:

		"""

		This method sets the zorder of the video.


		Parameters
		----------
		zorder : int
			Z order of the video.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    zorder = 2
			    ret = vid.set_zorder(zorder)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_position(self, position: List[float,float]) -> bool:

		"""

		This method sets the position (X,Y) of the video. Position of video refers to the relative coordinates of the video from the bottom left corner of the screen. This method works for the active page.


		Parameters
		----------
		position : list[float,float]
			Position of the video.
			A list with doubles: 
			[0]: X position
			[1]: Y position

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    position = [0.5, 0.4]
			    ret = vid.set_position(position)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_center(self, center: List[float,float]) -> bool:

		"""

		This method sets the center (X,Y) of the video. Center of video refers to the relative coordinates of the center point of the video from the bottom left corner. This method works for the active page.


		Parameters
		----------
		center : list[float,float]
			Center of the image. 
			A list with doubles:
			[0]: X position
			[1]: Y position

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    center = [0.4, 0.8]
			    ret = vid.set_center(center)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_scale(self, scale: List[float,float]) -> bool:

		"""

		This method sets the scale factor (X,Y) of the video. Scale factor refers to the original size of the video and it is a value greater than zero. This method works for the active page.


		Parameters
		----------
		scale : list[float,float]
			Scale factors of the video. 
			A list with doubles:
			[0]: X scale factor
			[1]: Y scale factor

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    scale = [0.6, 0.8]
			    ret = vid.set_scale(scale)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_settings(self, settings: dict) -> bool:

		"""

		This method sets the settings of the video. This method works for the active page.


		Parameters
		----------
		settings : dict
			Settings (key-value) of the image.
			A dictionary with string keys and string values:
			- 'align': Align Video to Window ('bottom', 'top', 'left', 'right', 'center')
			- 'align_hoffset': Horizontan offset (float)
			- 'align_voffset': Vertical offset (float)
			- 'autoscale': Scale with window resize (0,1)
			- 'filter': Video Processing filters ('none', 'red', 'green', 'blue', 'emboss', 'hardedge', 'highlight', 'sharpen', 'softedge'')
			- 'filter_transparent': Transparency (integer)
			- 'swaprgb': Swap Video Colors (0,1)
			- 'pixel_aspect': Pixel Aspect ratio (float)
			- 'zorder': Z order (integer)

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    settings = {
			        "align": "right",
			        "align_hoffset": 1.0,
			        "align_voffset": 1.0,
			        "autoscale": 0.2,
			        "filter": "red",
			        "filter_transparent": 20,
			        "swaprgb": 0.2,
			        "pixel_aspect": 1.2,
			        "zorder": 2,
			    }
			    ret = vid.set_settings(settings)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def set_attribute(self, attribute_name: str, attribute_type: str, attribute_value: str) -> bool:

		"""

		This method sets the value of a specific user specified attribute of the video. If the given attribute does not exist it is automatically created and its value is set.


		Parameters
		----------
		attribute_name : str
			Name of the attribute.

		attribute_type : str
			Type of the attribute. 
			Its possible values are:
			'string': String
			'numerical': Number

		attribute_value : str
			Value of the attribute.
			Either a string, or a double depending on the attribute type.

		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    attribute_name = "test"
			    attribute_type = "numerical"
			    attribute_value = 22
			    ret = vid.set_attribute(attribute_type, attribute_name, attribute_value)
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def delete(self) -> bool:

		"""

		This method deletes the video.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    ret = vid.delete()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def show(self) -> bool:

		"""

		This method shows the video. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    ret = vid.show()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def hide(self) -> bool:

		"""

		This method hides the video. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    ret = vid.hide()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def select(self) -> bool:

		"""

		This method selects the video. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    ret = vid.select()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def deselect(self) -> bool:

		"""

		This method deselects the video. This method works for the active page.


		Returns
		-------
		bool
			Upon success, it returns True.Upon failure, it returns False.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    ret = vid.deselect()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def is_usable(self) -> bool:

		"""

		Checks if the object refers to a usable META Video entity.


		Returns
		-------
		bool
			Returns True if the Entity is usable. False otherwise.

		Examples
		--------
		::

			# PYTHON script
			import meta
			from meta import visuals
			
			
			def main():
			    vid = visuals.Video(name="video1", window_name="MetaPost", page_id=0)
			    ret = vid.is_usable()
			    print(ret)
			
			
			if __name__ == "__main__":
			    main()


		"""


	def __init__(self, name: str, window_name: str, page_id: int) -> None:

		"""

		Upon success it returns an object of class Video for the given video name, window name and page id.


		Parameters
		----------
		name : str
			Name of the video.

		window_name : str
			Name of the window.

		page_id : int
			Id of the page of the video.

		Returns
		-------
		None

		"""

