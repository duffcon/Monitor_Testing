#!/bin/bash

model=$(hwinfo --monitor | grep -m1 "Vendor: ")
vendor=$(hwinfo --monitor | grep -m1 "Model: ")

keys="Vendor;Model;\n"
echo -e $keys $model ';' $vendor > data.txt
