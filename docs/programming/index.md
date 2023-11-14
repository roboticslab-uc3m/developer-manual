# Programming

## Main Programming Tools

* YARP: See [Programming with YARP](programming-with-yarp.md).
* C/C++: Low-level (control) programming. See [below](#programming-in-cc).
* CMake: See [below](#programming-in-cmake).
* Python: High-level (algorithm) programming.
* Doxygen: Document code, within the code.
    * Related issue: ["Program documentation: md vs dox" (qa#29)](https://github.com/roboticslab-uc3m/questions-and-answers/issues/29)
* You can find more general recommendations for programming at: [Programación (Spanish)](https://asrob.uc3m.es/tutoriales/software/programming/index.html)

## General Programming

* In case of trouble during installation of dependencies or additional software, take a look first at our dedicated repository: [installation-guides](https://github.com/roboticslab-uc3m/installation-guides) ([gitbook](https://robots.uc3m.es/installation-guides/)).
* If incorporating a new dependency or additional software, first take a look at our dedicated repository: [installation-guides](https://github.com/roboticslab-uc3m/installation-guides) ([gitbook](https://robots.uc3m.es/installation-guides/)). If it's not there, consider if it's a good option using the following recommended (but not mandatory) criteria: lightweight, flexible, multiplatform. If so, add it there, then link it to your project.
* Indent your code as if everything were Python. [astyle](http://astyle.sourceforge.net/) can handle this quite automatically for you \(use with caution\).
* Any `toDo`, `fixMe`, etc. inlined in code must be associated to an _open issue_ \(with bidirectional reference\).
* [Headers, config files and CLI parameters](https://github.com/roboticslab-uc3m/asibot-main/blob/master/doc/asibot-post-install.md#changing-parameters).
* Read about [Clean code](https://www.google.es/search?q=cleancode).
* We use [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) and [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration).
* Let's repeat:
    * DON'T ADD DIGITS to filenames as a hint of a specific version, iteration step, etc. - version control is for this.
    * AVOID DUPLICATES of existing files and programs: [don't repeat yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Prior to creating a new program, thoroughly analyze whether you can enhance an existing one through adjustment or implementation of new parameters. Once you are sure that the functionality of a program could be extended, proceed with the usual steps \(open an issue or fork & create a pull request\).

## Programming in CMake

* [Tutorial (Spanish)](https://asrob.uc3m.es/tutoriales/software/programming/cmake.html)
* Naming conventions:
    * *SCREAMING\_SNAKE\_CASE* for the project name, files and configuration variables: `TEO_MAIN`, `TEO_MAINConfig.cmake.in`, `TEO_MAIN_INCLUDE_DIRS`.
    * *kebab-case* for installed YARP context directories as set by `yarp_configure_external_installation()`: `teo-main`, `asibot-openrave-models`.
    * Use the `ROBOTICSLAB_` (or `roboticslab-`) prefix whenever the uniqueness of the chosen name for the project could be easily compromised (keep in mind you'll want to invoke `find_package()`): `ROBOTICSLAB_YARP_DEVICES`, `ROBOTICSLAB_KINEMATICS_DYNAMICS_INCLUDE_DIRS`, `roboticslab-vision`.

## Programming in C/C++

* Some good slides on C are "Thinking in C" by Bruce Eckel, and some good books on C++ are "Thinking in C++" by Bruce Eckel.
* A nice IDE is QTCreator, but you can also customize Eclipse, Atom or even Vim.
* Use [project-generator](https://github.com/roboticslab-uc3m/project-generator) for creation of new C/C++ projects.
* Report any problems with project-generator in its corresponding [issues section](https://github.com/roboticslab-uc3m/project-generator/issues). If you find that this solution doesn't suit you, at least stick to [CMake]((#programming-in-cmake) for any C/C++ project.
* Use _UpperCamelCase_ for library and class names.
* Use _lowerCamelCase_ for executable names.
* Avoid global variables.
* We prefer modern `std::string` class to alternatives like `char*` or `yarp::os::ConstString`.
* Store your classes inside a _namespace_ block. Our current trend is `roboticslab::` (see https://github.com/roboticslab-uc3m/QA/issues/15).
* Keep a minimalistic `main()` by implementing your program as an OOP class, see comments on `RFModule` in best practices in [Programming with YARP](programming-with-yarp.md).
* Create and maintain unit tests for each class. We are currently using **gtest**, see [kinematics-dynamics/tests/testKdlSolver](https://github.com/roboticslab-uc3m/kinematics-dynamics/tree/master/tests/testKdlSolver.cpp), which is then integrated with Travis CI.
* It is recommended to mark a function as DEPRECATED for a month before eliminating it from an API. DEPRECATED macros can be generated via CMake as done [here](https://github.com/roboticslab-uc3m/kinematics-dynamics/blob/21f2dde2a38f1d0c1c93703d3619e34c14c3bfcd/CMakeLists.txt#L110-L118), then used within code as [here](https://github.com/roboticslab-uc3m/kinematics-dynamics/blob/21f2dde2a38f1d0c1c93703d3619e34c14c3bfcd/libraries/TeoYarp/ICartesianSolver.h#L29-L33). The full procedure, as described at [QA #21](https://github.com/roboticslab-uc3m/QA/issues/21), should be:
    1. Open a [GitHub Issue](github.md#github-issues) wherever the offending function is located.
    1. Label it as `announcement`.
    1. Use the search bar to localize any call to said function across roboticslab-uc3m and list all affected repos.
    1. If necessary, elaborate a removal plan and detail any steps that need to be taken to perform a seamless migration to the new API.
    1. Ping the corresponding team or whoever could need more action on their end.
    1. Proceed gradually and, finally, kill the function.
* Always initialize class members, either in the class constructor or in any initialization method (e.g. your implementation of `DeviceDriver::open` when creating custom _YARP devices_) before doing the actual work.
* More links to best practices:
    * <https://github.com/google/eng-practices>
    * <https://google.github.io/styleguide/cppguide.html>
    * <https://www.perforce.com/resources/qac/high-integrity-cpp-coding-standard>

## If you have any doubts or comments

Please read the [Asking Questions](asking-questions.md) section, and once you've succeded with its [self-evaluation](asking-questions.md#self-evaluation-time) follow the recommendations by commenting publicly [HERE](https://github.com/roboticslab-uc3m/developer-manual/issues/new) if required.
