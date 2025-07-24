# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_atom_qs_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED atom_qs_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(atom_qs_FOUND FALSE)
  elseif(NOT atom_qs_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(atom_qs_FOUND FALSE)
  endif()
  return()
endif()
set(_atom_qs_CONFIG_INCLUDED TRUE)

# output package information
if(NOT atom_qs_FIND_QUIETLY)
  message(STATUS "Found atom_qs: 0.0.0 (${atom_qs_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'atom_qs' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${atom_qs_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(atom_qs_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${atom_qs_DIR}/${_extra}")
endforeach()
