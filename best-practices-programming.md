# Best Practices: Programming

* [Main Programming Tools](#main-programming-tools)
* [General Programming](#general-programming)
* [Programming in CMake](#programming-in-cmake)
* [Programming in C/C++](#programming-in-cc)
* [Programming in C++ with YARP](#programming-in-c-with-yarp)
* [If you have any doubts or comments](#if-you-have-any-doubts-or-comments)

## Main Programming Tools
* YARP: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/programming/yarp.html). Best practices ([below](#programming-in-c-with-yarp)).
* C/C++: Low-level (control) programming. Some good slides on C are "Thinking in C" by Bruce Eckel, and some good books on C++ are "Thinking in C++" by Bruce Eckel. A nice IDE is QTCreator, but you can also customize Eclipse, Atom or even Vim. Best practices ([below](#programming-in-cc)).
* CMake: [Tutorial (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/programming/cmake.html). Best practices ([below](#programming-in-cmake))
* Python: High-level (algorithm) programming.
* Doxygen: Document code, within the code.
    * Related issue: ["Program documentation: md vs dox" (qa#29)](https://github.com/roboticslab-uc3m/questions-and-answers/issues/29)
* You can find more general recommendations for programming at: [Programación (Spanish)](https://asrob-uc3m.gitbooks.io/tutoriales/content/software/programming/index.html)

## General Programming
* In case of trouble during installation of dependencies or additional software, take a look first at our dedicated repository: [installation-guides](https://github.com/roboticslab-uc3m/installation-guides) ([gitbook](http://robots.uc3m.es/gitbook-installation-guides)).
* If incorporating a new dependency or additional software, first take a look at our dedicated repository: [installation-guides](https://github.com/roboticslab-uc3m/installation-guides) ([gitbook](http://robots.uc3m.es/gitbook-installation-guides)). If it's not there, consider if it's a good option using the following recommended (but not mandatory) criteria: lightweight, flexible, multiplatform. If so, add it there, then link it to your project ([example](5182f9f475e229acea4cca1130be57489fd6b0f7)).
* Indent your code as if everything were Python. [astyle](http://astyle.sourceforge.net/) can handle this quite automatically for you \(use with caution\).
* Any `toDo`, `fixMe`, etc. inlined in code must be associated to an _open issue_ \(with bidirectional reference\).
* [Headers, config files and CLI parameters](https://github.com/roboticslab-uc3m/asibot-main/blob/develop/doc/asibot-post-install.md#changing-parameters).
* Read about [Clean code](https://www.google.es/search?q=cleancode).
* We use [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) and [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration).
* Let's repeat:
    * DON'T ADD DIGITS to filenames as a hint of a specific version, iteration step, etc. - version control is for this.
    * AVOID DUPLICATES of existing files and programs: [don't repeat yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Prior to creating a new program, thoroughly analyze whether you can enhance an existing one through adjustment or implementation of new parameters. Once you are sure that the functionality of a program could be extended, proceed with the usual steps \(open an issue or fork & create a pull request\).

## Programming in CMake
* Naming conventions:
  * *SCREAMING\_SNAKE\_CASE* for the project name, files and configuration variables: `TEO_MAIN`, `TEO_MAINConfig.cmake.in`, `TEO_MAIN_INCLUDE_DIRS`.
  * *kebab-case* for installed YARP context directories as set by `yarp_configure_external_installation()`: `teo-main`, `asibot-openrave-models`.
  * Use the `ROBOTICSLAB_` (or `roboticslab-`) prefix whenever the uniqueness of the chosen name for the project could be easily compromised (keep in mind you'll want to invoke `find_package()`): `ROBOTICSLAB_YARP_DEVICES`, `ROBOTICSLAB_KINEMATICS_DYNAMICS_INCLUDE_DIRS`, `roboticslab-vision`.

## Programming in C/C++
* Use [project-generator](https://github.com/roboticslab-uc3m/project-generator) for creation of new C/C++ projects.
* Report any problems with project-generator in its corresponding [issues section](https://github.com/roboticslab-uc3m/project-generator/issues). If you find that this solution doesn't suit you, at least stick to [CMake](http://asrob.uc3m.es/index.php/Tutorial_CMake) for any C/C++ project.
* Use _UpperCamelCase_ for library and class names.
* Use _lowerCamelCase_ for executable names.
* Avoid global variables.
* We prefer modern `std::string` class to alternatives like `char*` or `yarp::os::ConstString`.
* Store your classes inside a _namespace_ block. Our current trend is `roboticslab::` (see https://github.com/roboticslab-uc3m/QA/issues/15).
* Keep a minimalistic `main()` by implementing your program as an OOP class, see comments on `RFModule` in best practices in C++ with YARP ([below](#programming-in-c-with-yarp)).
* Create and maintain unit tests for each class. We are currently using **gtest**, see [kinematics-dynamics/test/testKdlSolver](https://github.com/roboticslab-uc3m/kinematics-dynamics/tree/develop/test/testKdlSolver.cpp) and [yarp-devices/tests/testTechnosoftIpos](https://github.com/roboticslab-uc3m/yarp-devices/tree/develop/tests/testTechnosoftIpos/testTechnosoftIpos.cpp), which is then integrated with Travis CI.
* It is recommended to mark a function as DEPRECATED for a month before eliminating it from an API. DEPRECATED macros can be generated via CMake as done [here](https://github.com/roboticslab-uc3m/kinematics-dynamics/blob/21f2dde2a38f1d0c1c93703d3619e34c14c3bfcd/CMakeLists.txt#L110-L118), then used within code as [here](https://github.com/roboticslab-uc3m/kinematics-dynamics/blob/21f2dde2a38f1d0c1c93703d3619e34c14c3bfcd/libraries/TeoYarp/ICartesianSolver.h#L29-L33). The full procedure, as described at [QA #21](https://github.com/roboticslab-uc3m/QA/issues/21), should be:
  1. Open an `issue` wherever the offending function is located.
  1. Label it as `announcement`.
  1. Use the search bar to localize any call to said function across roboticslab-uc3m and list all affected repos.
  1. If necessary, elaborate a removal plan and detail any steps that need to be taken to perform a seamless migration to the new API.
  1. Ping the corresponding team or whoever could need more action on their end.
  1. Proceed gradually and, finally, kill the function.
* Always initialize class members, either in the class constructor or in any initialization method (e.g. your implementation of `DeviceDriver::open` when creating custom _YARP devices_) before doing the actual work.
* More links to best practices:
   * https://github.com/google/eng-practices
   * https://google.github.io/styleguide/cppguide.html
   * https://www.perforce.com/resources/qac/high-integrity-cpp-coding-standard

## Programming in C++ with YARP
* We usually derive our base classes from [yarp::os::RFModule](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html), thus inheriting a [configure\(yarp::os::ResourceFinder& rf\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a6c3880961b00b0a7eb527d62214169b7) method that receives a map \([rf](http://www.yarp.it/classyarp_1_1os_1_1ResourceFinder.html)\) passed from `main()`, a [close\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a58ce26fc6fdcb6eb4af8e8dc678e095e) that gets called by _CRTL+C_, and a [updateModule\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#a37ee5baa17ce243458a1dff209e878b7) which is invoked with a periodicity measured in seconds given by [getPeriod\(\)](http://www.yarp.it/classyarp_1_1os_1_1RFModule.html#ace2fdadde1a2690f274079fabd6420d2). In case you need a function that gets called more often, you may inherit the [run\(\)](http://www.yarp.it/classyarp_1_1os_1_1PeriodicThread.html#a4585b8555a7b796aff7b2ba8b0c8343d) method from [yarp::os::PeriodicThread](http://www.yarp.it/classyarp_1_1os_1_1PeriodicThread.html) and obtain a periodicity given in seconds wih double precision, to be specified in the constructor.
* Implement your device as a class, and ideally as a [_YARP device_](http://asrob.uc3m.es/index.php/Tutorial_yarp_devices).

### Regarding `close()`
If there exists a `close` method that needs to release unmanaged resources (dynamically allocated memory) or terminate stuff in an ordered manner (if using `PolyDriver` class members, e.g. `close` device A before device B), always define a class destructor that calls `close`, be it a `DeviceDriver` or an `RFModule` derived class. Also, make sure nothing bad happens if this `close` method is called several times (i.e. set dangling pointers to `nullptr`). Why is that:
- `PolyDriver::open` may fail to initialize a subdevice, but it does not call the subdevice's `close` method; instead, it is immediately destructed via delete ([ref](https://github.com/robotology/yarp/blob/b3dff81c3739112b8f65cfd808f129bcbf4e7aa5/src/libYARP_dev/src/yarp/dev/PolyDriver.cpp#L308)).
- If `RFModule::configure` returns false, as explained in the above comments, `close` will never be called, hence we also want to use a destructor here.
- `PolyDriver::close` will never close a wrapped device twice, but callers of `RFModule` can do that inadvertently because of the previous point: once after a successful `RFModule::configure` and a `CTRL+C` signal (it just stops execution flow and calls close before leaving `runModule`), and one more time on class destruction.
- Despite those two mechanisms being relatively different, this policy ensures we treat both `RFModule` and `DeviceDriver` constructs in a similar manner: `close()` on destruction, avoid dangling pointers.


## If you have any doubts or comments
Please read the [Asking Questions](asking-questions.md) section, and once you've succeded with its [self-evaluation](asking-questions.md#self-evaluation-time) follow the recommendations by commenting publicly [HERE](https://github.com/roboticslab-uc3m/developer-manual/issues/new) if required
