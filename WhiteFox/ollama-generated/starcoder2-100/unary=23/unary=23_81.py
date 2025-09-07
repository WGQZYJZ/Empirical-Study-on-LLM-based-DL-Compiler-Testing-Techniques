t1 = softmax2d(input_tensor, dim=0) # Apply softmax to the 0th dimension in the input tensor
t3 = maxpooling(t2, kernel_size=[8], stride=None, padding=[16])# Max-pooling in the second dimension with a window size of 8. The padding is 16 on both sides
