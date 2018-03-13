cmake_minimum_required(VERSION 2.6)

project(ROBOTICSLAB_DEVELOPER_MANUAL)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

find_package(YARP REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${YARP_MODULE_PATH})
include(YarpInstallationHelpers)
yarp_configure_external_installation(roboticslab-developer-manual)

file(GLOB md ${CMAKE_SOURCE_DIR}/*.md)
file(GLOB en/md ${CMAKE_SOURCE_DIR}/en/*.md)
file(GLOB es/md ${CMAKE_SOURCE_DIR}/es/*.md)

yarp_install(FILES ${md} DESTINATION ${ROBOTICSLAB-DEVELOPER-MANUAL_CONTEXTS_INSTALL_DIR})
yarp_install(FILES ${en/md} DESTINATION ${ROBOTICSLAB-DEVELOPER-MANUAL_CONTEXTS_INSTALL_DIR}/en)
yarp_install(FILES ${es/md} DESTINATION ${ROBOTICSLAB-DEVELOPER-MANUAL_CONTEXTS_INSTALL_DIR}/es)

include(GNUInstallDirs)

if(WIN32 AND NOT CYGWIN)
    set(_cmake_destination CMake)
else()
    set(_cmake_destination ${CMAKE_INSTALL_LIBDIR}/cmake/ROBOTICSLAB_DEVELOPER_MANUAL)
endif()

export(PACKAGE ROBOTICSLAB_DEVELOPER_MANUAL)

file(WRITE ${CMAKE_BINARY_DIR}/ROBOTICSLAB_DEVELOPER_MANUALConfig.cmake "# Dummy CMake configuration export file.")
install(FILES ${CMAKE_BINARY_DIR}/ROBOTICSLAB_DEVELOPER_MANUALConfig.cmake DESTINATION ${_cmake_destination})

include(AddUninstallTarget)
