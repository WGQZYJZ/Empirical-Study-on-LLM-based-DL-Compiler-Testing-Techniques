Note that for `lowmem_dropout` we do not invoke a node replacing operation in this case. This is because a node invoking a lowmem function cannot trigger a replacement as the graph already contains one, and thus we need to directly invoke the replacement.

