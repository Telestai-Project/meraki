add_executable(lightverify lightverify.cpp)
target_link_libraries(lightverify PRIVATE meowpow)
target_include_directories(lightverify PRIVATE ${MEOWPOW_PRIVATE_INCLUDE_DIR})
set_target_properties(lightverify PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)