t1 = ConvTranspose2d(input_channels=10, output_channels=8) # Apply transposed convolution to the input tensor with 10 input channels and 8 output channels (kernel size 5, stride 3).
t2 = torch.nn.ReLU() # Applies the ReLU activation function to the input of the previous operation.
t1 = Linear(input_features=3072) # Apply linear transformation to the input with 3072 features (flattening the image in the case of a 64x64 image).
t2 = ReLU() # Applies the ReLU activation function to the output of the previous operation.
