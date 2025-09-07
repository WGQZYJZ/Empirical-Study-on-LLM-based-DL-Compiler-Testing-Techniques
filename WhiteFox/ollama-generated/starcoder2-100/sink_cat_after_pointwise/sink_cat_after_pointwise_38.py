t1 = input_tensor[...]  # Subslice an input tensor by slicing out the 4th channel from its 3rd dimension.
t2 = torch.nn.functional.conv3d(t1, ...)  # Apply a 3D convolution on the sub-sliced input tensor t1.
