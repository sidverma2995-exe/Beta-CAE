from __future__ import annotations
from typing import Iterable, Callable, Any
import warnings
import typing_extensions

class VR():

	"""

	A VR object allows you to access tracking data of VR devices as well as set callbacks for the vr controllers buttons press and release.

	Notes
	-----
	VR devices are separated into following classes:
	"HMD" - Head Mounted Display. There can only be one such device and it has always an index of 0.
	"Controller" - The controllers users hold in their hands. There can be up to two such devices.
	"GenericTracker" - Similar to controllers, but used to track a position of an object.
	"TrackingReference" - Cameras and/or base stations that serve as tracking reference points.
	"DisplayRedirect" - Accessories that aren't necessarily tracked themselves, but may redirect video output from other tracked devices.
	
	Each VR device can be in one of the following states:
	"Unknown"
	"Idle" - No activity for the last 10 seconds
	"UserInteraction" - Activity is happening now. The device is moving.
	"UserInteractionTimeout" - No activity for the last 0.5 seconds
	"Standby" - Device in standby mode. The exact time to enter standby is configurable.

	Examples
	--------
	::

		import ansa
		from ansa import vr
		from ansa import guitk
		
		
		class UpdateFrame:
		    def __init__(self, vr):
		        self.vr = vr
		
		    def __call__(self):
		        for device in self.vr.tracked_devices():
		            if (
		                self.vr.device_status(device) == "UserInteraction"
		                or self.vr.device_status(device) == "UserInteractionTimeout"
		            ):
		                pose = self.vr.device_pose(device)
		                if pose["valid"] == True and pose["device_connected"] == True:
		                    print(self.vr.device_type(device))
		                    print(pose["pose"])
		
		
		def main():
		    vr = ansa.vr.VR()
		    vr.track_devices(("Controller", "HMD"))
		    vr.tracking_update(UpdateFrame(vr))
		
		
		if __name__ == "__main__":
		    main()
		import ansa
		from ansa import vr
		
		
		class ButtonCommand:
		    def pressFuncExecute(self):
		        print("Pressed primary execute")
		
		    def unpressFuncExecute(self):
		        print("Released primary execute")
		
		    def pressFuncExecuteSecondary(self):
		        print("Pressed secondary execute")
		
		    def unpressFuncExecuteSecondary(self):
		        print("Released secondary execute")
		
		    def pressFuncPin(self):
		        print("Pressed primary pin")
		
		
		def main():
		    vr = ansa.vr.VR()
		    cmd = ButtonCommand()
		    vr.enable_callbacks("Test")
		    vr.button_press_callback(
		        "VR_BUTTON_TRIGGER", True, cmd.pressFuncExecute, "Primary Execute"
		    )
		    vr.button_release_callback(
		        "VR_BUTTON_TRIGGER", True, cmd.unpressFuncExecute, "Primary Execute"
		    )
		    vr.button_press_callback(
		        "VR_BUTTON_TRIGGER", False, cmd.pressFuncExecuteSecondary, "Secondary Execute"
		    )
		    vr.button_release_callback(
		        "VR_BUTTON_TRIGGER", False, cmd.unpressFuncExecuteSecondary, "Secondary Execute"
		    )
		    vr.button_press_callback("VR_BUTTON_GRIP", True, cmd.pressFuncPin, "Primary Pin")
		
		
		if __name__ == "__main__":
		    main()

	"""


	is_running: bool = None
	"""
	Query if vr is running.

	"""

	def __init__(self) -> None:

		"""

		VR object constructor.


		Returns
		-------
		None

		"""


	def device_type(self, device: int) -> str:

		"""

		Get the class of a VR Device.Possible classes are: "HMD", "Controller", "GenericTracker", "TrackingReference", "DisplayRedirect", "Invalid".


		Parameters
		----------
		device : int
			The index of a tracked device

		Returns
		-------
		str
			Return the class name of the VR Device.

		"""


	def device_status(self, device: int) -> str:

		"""

		Get the status of a VR Device.Possible values are: "Unknown", "Idle", "UserInteraction", "UserInteractionTimeout", "Standby".


		Parameters
		----------
		device : int
			The index of a tracked device

		Returns
		-------
		str

		"""


	def device_position(self, device: int) -> object:

		"""

		Get the position of a VR Device.


		Parameters
		----------
		device : int
			The index of a tracked device.

		Returns
		-------
		object
			Returns a tuple with the coordinates of the device position in 3D space.

		"""


	def devices(self) -> list[int]:

		"""

		Get a list of indices of all Devices


		Returns
		-------
		list[int]
			Returns a list containing the indices of all connected vr devices.

		"""


	def tracked_devices(self) -> list[int]:

		"""

		Get a list of indices of tracked devices.


		Returns
		-------
		list[int]
			Returns a list containing the indices of all tracked vr devices.

		"""


	def tracking_update(self, callback: object) -> None:

		"""

		Set callback for tracking data update.


		Parameters
		----------
		callback : object
			A callback object which is called on each tracking update.

		Returns
		-------
		None
			Always returns None.

		"""


	def track_devices(self, device_types: object) -> None:

		"""

		Select which class of devices to track.


		Parameters
		----------
		device_types : object
			Possible values : "HMD", "Controller", "GenericTracker", "TrackingReference", "DisplayRedirect", "All"

		Returns
		-------
		None
			Always returns None.

		"""


	def device_pose(self, device: int) -> dict:

		"""

		Get the pose of a VR Device.


		Parameters
		----------
		device : int
			The index of a tracked device.

		Returns
		-------
		dict
			Returns a dictionary containing a pose frame of a device. It consists of the following fields:"pose" : a column major 4x4 matrix of the device pose in 3D space."valid" : a boolean flag, true if the tracking pose data are valid."device_connected" : a boolean flag, true if device with the given index is connected.

		"""


	def display_notification(self, message: str, persistent: bool) -> None:

		"""

		Display a notification message


		Parameters
		----------
		message : str
			A text message to display.

		persistent : bool, optional
			If set to true, the notification is persistent, it is dismissable by a button press. If set to false the notification will disappear automatically after a few seconds. Default is false.

		Returns
		-------
		None
			Always returns None.

		"""


	def show_devices(self, devices: object, visible: bool) -> None:

		"""

		Toggle drawing of a device class


		Parameters
		----------
		devices : object
			Possible values : "HMD", "Controller", "GenericTracker", "TrackingReference", "DisplayRedirect", "All"

		visible : bool
			Boolean to show/hide the drawing of the devices of the specified class.

		Returns
		-------
		None
			Always returns None.

		"""


	def enable_callbacks(self, name: str) -> None:

		"""

		Enable vr controllers buttons callbacks


		Parameters
		----------
		name : str

		Returns
		-------
		None
			Always returns None.

		"""


	def disable_callbacks(self) -> None:

		"""

		Disable vr controllers buttons callbacks


		Returns
		-------
		None
			Always returns None.

		"""


	def button_press_callback(self, action: str, primary: bool, callback: object, tooltip: str) -> None:

		"""

		Set press callback for a vr controller button


		Parameters
		----------
		action : str
			The button for which the callback will be set. The available buttons are: 
			"VR_BUTTON_TOUCHPAD"
			"VR_BUTTON_GRIP"
			"VR_BUTTON_TRIGGER"
			"VR_BUTTON_LEFT"
			"VR_BUTTON_RIGHT"
			"VR_BUTTON_UP"
			"VR_BUTTON_DOWN"

		primary : bool
			Select primary or secondary controller

		callback : object
			The callable object which will be called on button press.

		tooltip : str, optional
			The tooltip to display next to the controller button, when script callbacks are enabled.

		Returns
		-------
		None
			Always returns None.

		"""


	def button_release_callback(self, action: str, primary: bool, callback: object, tooltip: str) -> None:

		"""

		Set release callback for a vr controller button


		Parameters
		----------
		action : str
			The button for which the callback will be set. The available buttons are: 
			"VR_BUTTON_TOUCHPAD"
			"VR_BUTTON_GRIP"
			"VR_BUTTON_TRIGGER"
			"VR_BUTTON_LEFT"
			"VR_BUTTON_RIGHT"
			"VR_BUTTON_UP"
			"VR_BUTTON_DOWN"

		primary : bool
			Select primary or secondary controller.

		callback : object
			The callable object which will be called on button release.

		tooltip : str, optional
			The tooltip to display next to the controller button, when script callbacks are enabled.

		Returns
		-------
		None
			Always returns None.

		"""


	def move_head(self, x: float, y: float, z: float, offset: float) -> None:

		"""

		Move the head to a specified position in world coordinates


		Parameters
		----------
		x : float
			X coordinate of the position to move the head.

		y : float
			Y coordinate of the position to move the head.

		z : float
			Z coordinate of the position to move the head.

		offset : float, optional
			an offset from the position to move the head.

		Returns
		-------
		None
			Always returns None.

		"""

