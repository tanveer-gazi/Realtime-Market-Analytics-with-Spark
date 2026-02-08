# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 01:17:48 2024

@author: ISGA 
"""
import time
counter = 0
string_buffer = ""

while True:
    with open("tmp/log-generator.log", "r") as log_file:
        for line in log_file:
            if counter == 0:
                string_buffer = ""
            
            string_buffer += f"\n{line}"
            counter += 1
            
            if counter == 1000:
                today = time.strftime("%Y_%m_%d_%H_%M_%S")
                filename = f"src/main/resources/data/{today}.log"
                with open(filename, "w") as output_file:
                    output_file.write(string_buffer)
                counter = 0
