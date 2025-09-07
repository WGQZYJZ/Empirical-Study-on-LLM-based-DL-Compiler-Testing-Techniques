t1 = conv(input_tensor, kernel=[3] * 5 + [2]) # Apply a convolutional layer with kernel size 3 followed by five additional kernel sizes and then another one. The resulting output is passed to an average pooling function.
t2 = linear(t1) # Apply the fully connected (or dense) layer that takes as input the flattened output of the previous convolutional layer. This dense layer has a width of 4096.
