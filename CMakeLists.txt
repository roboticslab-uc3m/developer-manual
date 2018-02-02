# Bare cmake

cmake_minimum_required(VERSION 2.6)

set(KEYWORD "best-practices")

# Start a project.
project(${KEYWORD})

find_package(YARP REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${YARP_MODULE_PATH})
include(YarpInstallationHelpers)
yarp_configure_external_installation(roboticslab-developer-manual)

file(GLOB md ${CMAKE_CURRENT_SOURCE_DIR}/*.md)
file(GLOB en/md ${CMAKE_CURRENT_SOURCE_DIR}/en/*.md)
file(GLOB es/md ${CMAKE_CURRENT_SOURCE_DIR}/es/*.md)

yarp_install(FILES ${md} DESTINATION ${ROBOTICSLAB-BEST-PRACTICES_CONTEXTS_INSTALL_DIR})
yarp_install(FILES ${en/md} DESTINATION ${ROBOTICSLAB-BEST-PRACTICES_CONTEXTS_INSTALL_DIR}/en)
yarp_install(FILES ${es/md} DESTINATION ${ROBOTICSLAB-BEST-PRACTICES_CONTEXTS_INSTALL_DIR}/es)

# uninstall target
configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/template/ROBOTICSLAB_BEST_PRACTICESConfigUninstall.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/ROBOTICSLAB_BEST_PRACTICESConfigUninstall.cmake" IMMEDIATE @ONLY)

add_custom_target(uninstall
    COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/ROBOTICSLAB_BEST_PRACTICESConfigUninstall.cmake)

