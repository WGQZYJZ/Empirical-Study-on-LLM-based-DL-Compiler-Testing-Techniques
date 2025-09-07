t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5             # Multiply the output of the convolution by 0.5
t3 = torch.relu(other)    # Apply ReLU activation function on another input to the model, and then multiply its result by 0.7071067811865476 to find a new value
