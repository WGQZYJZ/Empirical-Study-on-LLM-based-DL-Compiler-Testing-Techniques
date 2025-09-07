t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5  # Multiply the output of the convolution by 0.5
t3 = torch.nn.Conv2d(in_channels, out_channels=outc, kernel_size=ks, stride=1, padding=(ks-1)//2)
