# it is possible to parallelize the find_wellformed_subchain function 
# for processing very long chains that don't fit in memory, for example we can 
# split the chain into smaller strings and use those as an input for multiple 
# machines running the function and then add the result of each of the return
# values of these machines to get the total length.

# this also brings a significant improvement to the processing time, where it 
# would be dependent on the number of machines used, although some overhead should
# be consdered to distribute the task among the machines, to add up the result at 
# the end of processing, and for communication between the machines in general.