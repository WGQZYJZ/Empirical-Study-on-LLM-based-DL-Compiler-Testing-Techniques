t0 = conv(input_tensor) # Apply pointwise convolution with kernel size 3 to the input tensor
t1 = torch.nn.functional.layer_norm(input=t0, normalized_shape=[784], eps=eps)  # Apply the Layer Normalization operation along dimensions [784] of the specified epsilon for the input t0
