t0 = dropout(input_tensor) * 2 # Multiplying output by a constant value 2 using torch.nn.Dropout and torch.nn.functional.dropout()
t1 = nn.Conv2d(3,8,(4,3),(2,1), padding=(1, 1))(t0) # Applying 3x3 convolution with kernel_size= (4,3), stride=(2,1), padding=(1, 1). The input tensor is a 64 x 64 image.
t2 = nn.Dropout2d()(t1) * 0.5 + 0.7 # Applying torch.nn.Dropout2d and applying constant 0.7 to the output of the convolution operation. The input tensor is 8 x 32 x 32 image.
t0 = nn.Dropout2d()(input_tensor) * 3 # Applying torch.nn.Dropout2d and multiplying output by a constant value 3. The input tensor is 64 x 64 image.
t1 = nn.Conv2d(8, (7,5), padding=(0, 1))(t0) + 4 # Convolving an 8 x 64 x 64 image with a kernel size of (7,5). The padding is equal to one on the left side and zero on the right side.
