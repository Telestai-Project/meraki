add_executable(meraki meraki.cpp)

target_link_libraries(meraki PRIVATE meraki -levent)
target_include_directories(meraki PRIVATE ${MERAKI_PRIVATE_INCLUDE_DIR})
set_target_properties(meraki PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)