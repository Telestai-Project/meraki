# meraki: C/C++ implementation of Meraki, the Telestai Proof of Work algorithm.
# Copyright 2018-2019 Pawel Bylica.
# Licensed under the Apache License, Version 2.0.

add_executable(kiss99-tester kiss99_tester.cpp)
target_link_libraries(kiss99-tester PRIVATE meraki)
target_include_directories(kiss99-tester PRIVATE ${MERAKI_PRIVATE_INCLUDE_DIR})
set_target_properties(kiss99-tester PROPERTIES RUNTIME_OUTPUT_DIRECTORY ..)
