cmake_minimum_required(VERSION 3.12)

# Define a project.
project(ROBOTICSLAB_DEVELOPER_MANUAL LANGUAGES NONE)

# Find dependencies
find_package(YCM 0.10 REQUIRED)
find_package(YARP 3.0 REQUIRED)

# Set some useful variables - paths relative to the installation prefix.
yarp_configure_external_installation(roboticslab-developer-manual)

# Install docs, and also create a copy in the local build tree.
yarp_install(DIRECTORY docs
             DESTINATION ${ROBOTICSLAB-DEVELOPER-MANUAL_CONTEXTS_INSTALL_DIR})

# Store the package in the user registry.
set(CMAKE_EXPORT_PACKAGE_REGISTRY ON)

# Create and install config files.
include(InstallBasicPackageFiles)

install_basic_package_files(ROBOTICSLAB_DEVELOPER_MANUAL
                            VERSION 0.1.0
                            COMPATIBILITY AnyNewerVersion
                            NO_EXPORT)

# Add uninstall rule.
include(AddUninstallTarget)
