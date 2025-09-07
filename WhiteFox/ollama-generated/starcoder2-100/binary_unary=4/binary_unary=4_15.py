  t3 = torch.nn.AvgPool2d(kernel_size=2)  # Apply average pooling to the input tensor, with a kernel size of 2
  t4 = torch.nn.Upsample(scale_factor=0.5, mode='bilinear')  # Resize the output of the average pooling operation by 1/2 and apply bilinear interpolation on it.
