t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = torch.leaky_relu_(t1, alpha=0.5) # Applies the leaky ReLU function to the output of the convolution operation using an additional input parameter
