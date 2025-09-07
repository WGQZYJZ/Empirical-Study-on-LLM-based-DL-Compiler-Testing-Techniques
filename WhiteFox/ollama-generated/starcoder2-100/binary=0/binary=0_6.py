t0 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor.
t1 = torch.nn.Linear(output_channels, 256)(t0) + 4*other # The output of the linear layer is added to another tensor that's scaled by a constant 4
