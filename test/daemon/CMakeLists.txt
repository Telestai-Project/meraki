add_executable(meowpow meowpow.cpp)

target_link_libraries(meowpow PRIVATE meowpow -levent)
target_include_directories(meowpow PRIVATE ${MEOWPOW_PRIVATE_INCLUDE_DIR})
set_target_properties(meowpow PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)