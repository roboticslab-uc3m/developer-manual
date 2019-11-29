# Frequently Asked Questions (FAQ)

* [Which Operating System should I use?](#which-operating-system-should-i-use)
* [I was told to install something. How can I do that?](#i-was-told-to-install-something-how-can-i-do-that)
* [I see a lot of commands for installation but do not understand anything. What do they mean?](#i-see-a-lot-of-commands-for-installation-but-do-not-understand-anything-what-do-they-mean)
* [I've heard lots of stuff about Git and GitHub. What do they mean?](#ive-heard-lots-of-stuff-about-git-and-github-what-do-they-mean)
* [How should I programm stuff?](#how-should-i-programm-stuff)
* [How should I document stuff?](#how-should-i-document-stuff)
* [How can I record data for Programming by Demonstration (PbD) a.k.a. Learning from Demonstration (LfD)?](#how-can-i-record-data-for-programming-by-demonstration-pbd-aka-learning-from-demonstration-lfd)
* [How can I play back data recorded for Programming by Demonstration (PbD) a.k.a. Learning from Demonstration (LfD)?](#how-can-i-play-back-data-recorded-for-programming-by-demonstration-pbd-aka-learning-from-demonstration-lfd)
* [How does the iPos PT Mode work?](#how-does-the-ipos-pt-mode-work)
* [How can I change the RGB-D sensor resolution?](#how-can-i-change-the-rgb-d-sensor-resolution)
* [I've found some broken links in your repositories, which have been renamed?](#ive-found-some-broken-links-in-your-repositories-which-have-been-renamed)
* [If you have any doubts or comments](#if-you-have-any-doubts-or-comments)

## Which Operating System should I use?
- For desktops and laptops, we recommend a GNU/Linux ([what is Linux? (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/linux/introduction.html#%C2%BFqu%C3%A9-es-linux)) distribution ([what is a distribution? (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/linux/introduction.html#%C2%BFqu%C3%A9-es-una-distribuci%C3%B3n-de-linux)) on a native partition ([what options do I have to install a distribution? (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/linux/introduction.html#%C2%BFqu%C3%A9-opciones-tengo-para-instalar-una-distribuci%C3%B3n) and [how to install a native partition (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/linux/introduction.html#%C2%BFc%C3%B3mo-instalo-una-distribuci%C3%B3n-en-una-partici%C3%B3n-nativa)). The specific GNU/Linux distribution we recommend is [Ubuntu](https://ubuntu.com/#download) (`Ubuntu Desktop`). You are free to choose between  version `16.04 LTS ` and `18.04 LTS`. Either one is a good option, although we have slight more support for `16.04`.
- For robot on-board CPUs, you can read through a long conversation at: [questions-and-answers#20](https://github.com/roboticslab-uc3m/questions-and-answers/issues/20). 

## I was told to install something. How can I do that?
- Please make sure you carefully read and understood the dedicated section at: [how do I install programs on Linux? (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/linux/introduction.html#¿cómo-instalo-programas-en-linux)
- Each of our repositories usually contains instructions for installing, e.g. the initial `README.md` of <https://github.com/roboticslab-uc3m/vision> links to its [doc/vision-install.md](https://github.com/roboticslab-uc3m/vision/blob/develop/doc/vision-install.md) documentation file.
   - Note 1: Don't know what a repository is? Please read: [Control de versiones (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/version-control/index.html)
   - Note 2: This manual contains an index of our repositories: [HERE](appendix/repository-index.md)
- For instructions on installing 3rd party software, please see a special repository we maintain: <http://robots.uc3m.es/gitbook-installation-guides>

## I see a lot of commands for installation but do not understand anything. What do they mean?
- Please read: [Linux - Bash (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/linux/bash.html)

## I've heard lots of stuff about Git and GitHub. What do they mean?
- Please read:
   - [Git y GitHub (Spanish)](https://david-estevez.gitbooks.io/the-git-the-bad-and-the-ugly/content/es/control-de-versiones.html)
   - [Control de versiones - Git (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/version-control/git.html)

## How should I programm stuff?
- C/C++: Low-level (control) programming. Some good slides on C are "Thinking in C" by Bruce Eckel, and some good books on C++ are "Thinking in C++" by Bruce Eckel. A nice IDE is QTCreator, but you can also customize Eclipse, Atom or even Vim. 
- CMake: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/programming/cmake.html)
- Python: High-level (algorithm) programming.
- Doxygen: Document code, within the code.

## How should I document stuff?
- Markdown: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/writing/markdown.html)

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

## How does the iPos PT Mode work?

`PT Mode` performs at a fixed rate at driver level. This is great, because it's real-time right next to the motor, so network latencies will not affect performance of set of a pre-defined joint-space targets (positions). Not justifying how it's implemented, but providing the reason why they actually did it as it is. Naïve options:
1. First receive (e.g. via CAN-bus) all the trajectory, then execute each target at the exact time given the fixed period. The issue with this is: how much memory should we reserve for this? What happens if somebody wants to run a trajectory with thousands or millions of intermediate targets?
2. Receive the next target (e.g. via CAN-bus), execute it at exactly the planned time given the fixed period, repeat. The issue with this is: what happens if a target arrives late?

None of these options is the implemented solution. The iPos implementation is an intermediate solution, essentially a [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) memory with 8 buffer positions (would have to check the iPos manual for the specific correct value). So, you start filling it in, once it is initially full you start running, and then continue feeding it targets (e.g. via CAN-bus) at the rate established by the fixed period.
- If you feed it too slow, the buffer will empty before time and movement will stop.
- If you feed it too fast, the buffer will get full  (you'll see a `pt buffer full!` message in our [CanBusControlboard](https://github.com/roboticslab-uc3m/yarp-devices/blob/e696c219fa9aa6203d008585123ea477d9b74454/libraries/YarpPlugins/CanBusControlboard) implementation).

Hence, best to feed it at the most precise rate possible. Take into account that a [PeriodicThread](https://github.com/robotology/yarp/blob/master/example/os/ratethread.cpp) (YARP's old `RateThread`) will be more precise than adding a fixed delay at the end of your loop. 

In the current [CanBusControlboard](https://github.com/roboticslab-uc3m/yarp-devices/blob/e696c219fa9aa6203d008585123ea477d9b74454/libraries/YarpPlugins/CanBusControlboard) implementation, this is set when we instance the class, and may be modified via [--ptModeMs](https://github.com/roboticslab-uc3m/yarp-devices/blob/e696c219fa9aa6203d008585123ea477d9b74454/libraries/YarpPlugins/CanBusControlboard/DeviceDriverImpl.cpp#L10). You'll be asking yourself if there is a minimum threshold. The answer is yes, and this minimum should be estimated by the time consumed by CAN-bus communications to feed all the individual drivers per period.

## How can I change the RGB-D sensor resolution?
We use the YARP `OpenNI2DeviceServer` device for this. In [teoBase.xml#L36](https://github.com/roboticslab-uc3m/teo-configuration-files/blob/89d6e279d13cfe47c444c709cd7a08e5de56382b/share/teoBase/scripts/teoBase.xml#L36) you can see an example instance:
```bash
yarpdev --device OpenNI2DeviceServer --depthVideoMode 4 --colorVideoMode 9 --noRGBMirror
```
If you want to know what values you can use for `--depthVideoMode` and `--colorVideoMode` instead (and the actual meaning of the current values), please launch:
```bash
yarpdev --device OpenNI2DeviceServer --printVideoModes
```

## I've found some broken links in your repositories, which have been renamed?
Most of this was done at https://github.com/roboticslab-uc3m/questions-and-answers/issues/2
- https://github.com/roboticslab-uc3m/teo-body -> https://github.com/roboticslab-uc3m/yarp-devices
- https://github.com/roboticslab-uc3m/teo-head -> https://github.com/roboticslab-uc3m/vision and https://github.com/roboticslab-uc3m/speech
- https://github.com/roboticslab-uc3m/teo-main (old version) -> https://github.com/roboticslab-uc3m/kinematics-dynamics
- https://github.com/roboticslab-uc3m/best-practices -> https://github.com/roboticslab-uc3m/developer-manual
- https://github.com/roboticslab-uc3m/teo-software-manual -> https://github.com/roboticslab-uc3m/teo-developer-manual

## If you have any doubts or comments
Please read the [Asking Questions](asking-questions.md) section, and once you've succeded with its [self-evaluation](asking-questions.md#self-evaluation-time) follow the recommendations by commenting publicly [HERE](https://github.com/roboticslab-uc3m/developer-manual/issues/new) if required
