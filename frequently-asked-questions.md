# Frequently Asked Questions

## How can I record data for Programming by Demonstration (PbD) a.k.a. Learning from Demonstration (LfD)?

First, if moving the robot by hand, you'll want some gravity compensation to help out. That's `[gcmp]` off `BasicCartesianControl`. Refer to the [BasicCartesianControl documentation](http://robots.uc3m.es/dox-kinematics-dynamics/group__BasicCartesianControl.html) for reference.

Once you have publishing services running (robot joint/cartesian state, sensors output), there are two options for recording data:

1. Manually grab individual "waypoints" or sensor data and store in file(s). For instance, in the joint space, do some `yarp rpc /robotName/manipulatorName/rpc:i` to get joint positions.

1. To record full trajectories (data stream of a certain YARP port) at a given sample rate, use [yarpdatadumper](http://www.yarp.it/yarpdatadumper.html). To record from several YARP ports, [yarpdatadumperAppGenerator](http://www.yarp.it/yarpdatadumperAppGenerator.html) can be used to generate a [yarpmanager](http://www.yarp.it/yarpmanager.html) app of [yarpdatadumper](http://www.yarp.it/yarpdatadumper.html) components.

   An example of recording a left arm trayectory of TEO: 
   * Terminal 1:
   ```
   launchManipulation  # Part of teoBase
   ```
   * Terminal 2: 
   ```bash
   yarpdatadumper --name /leftArm  # the data.log and data.log files will be saved in a new `leftArm` directory
   ```
   * Terminal 3:
   ```bash
   yarp connect /teo/leftArm/state:o /leftArm
   ```

## How can I play back data recorded for Programming by Demonstration (PbD) a.k.a. Learning from Demonstration (LfD)?

Depending on options above:

1. You can use the waypoints in a program as in [this example](https://github.com/roboticslab-uc3m/yarp-devices/tree/73cbd201df69ee19662cdb26a83d898669834bcb/example/cpp/exampleRemoteControlboard).

1. Use stuff from our [tools](https://github.com/roboticslab-uc3m/tools) repository. Specifically, you'll want the [PlaybackThread](https://github.com/roboticslab-uc3m/tools/tree/a7be63dc53090a5ca4ed19dc078ab3823aac1be3/libraries/ToolsYarpPlugins/PlaybackThread). You can find an example of use at [examplePlaybackThread](https://github.com/roboticslab-uc3m/tools/tree/a7be63dc53090a5ca4ed19dc078ab3823aac1be3/example/cpp/examplePlaybackThread) and its corresponding [test](https://github.com/roboticslab-uc3m/tools/blob/a7be63dc53090a5ca4ed19dc078ab3823aac1be3/tests/testPlaybackThread/testPlaybackThread.cpp).

Note: There are several alternatives to these approaches, but these are kind of nice. [yarpmanager](http://www.yarp.it/yarpmanager.html) has some record/playback facilities, but we haven't really tried them. Additionally, [yarpdataplayer](http://www.yarp.it/yarpdataplayer.html) is the packaged YARP utility for playback. However, these interfaces have their playback capabilities tightly coupled to their GUI code. The previously mentioned components from the [tools](https://github.com/roboticslab-uc3m/tools) repository are lightweight and can be used independently as they are not coupled with any graphical interface.

## I've found some broken links in your repositories, which have been renamed?
Most of this was done at https://github.com/roboticslab-uc3m/questions-and-answers/issues/2
- https://github.com/roboticslab-uc3m/teo-body -> https://github.com/roboticslab-uc3m/yarp-devices
- https://github.com/roboticslab-uc3m/teo-head -> https://github.com/roboticslab-uc3m/vision
- https://github.com/roboticslab-uc3m/teo-main (old version) -> https://github.com/roboticslab-uc3m/kinematics-dynamics
- https://github.com/roboticslab-uc3m/best-practices -> https://github.com/roboticslab-uc3m/developer-manual
- https://github.com/roboticslab-uc3m/teo-software-manual -> https://github.com/roboticslab-uc3m/teo-developer-manual
