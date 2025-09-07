t1 = input_tensor[...]  # Get a slice with given start and stop indices
t2 = t3[..., ...i] # Get a slice along specific axis
t4 = t5[..., : , ..., i] # Get a slice along multiple axes. In this case, we use ellipsis to index as many axes as there are dimensions of the input tensor. The `...` in the slice indicates that all dimensions of the input tensor will be used to obtain a specific subsection from it.
