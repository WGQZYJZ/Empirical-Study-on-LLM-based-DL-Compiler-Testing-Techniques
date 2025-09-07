    t1  = torch.nn.Dropout(0.5)  # Apply dropout to the input tensor with probability `0.5`
    t2  = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1, output_padding=(1, 1))  # Apply pointwise transposed convolution operation on the input of size 6 x 7 with kernel of 3 x 3, stride (2, 2) and (1, 1) as the amount of zero columns/rows padded to both sides
