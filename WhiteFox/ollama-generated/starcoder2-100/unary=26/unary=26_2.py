t1  = torch.nn.ConvTranspose2d(3, 64 * k, 4 , stride=2, padding=1)(input_tensor) # Apply transposed convolution with kernel size 5 to the input tensor where k is an integer
t2 = t1 * 0.9876543210987654  # Multiply the output of the transposed convolution by 0.9876543210987654
