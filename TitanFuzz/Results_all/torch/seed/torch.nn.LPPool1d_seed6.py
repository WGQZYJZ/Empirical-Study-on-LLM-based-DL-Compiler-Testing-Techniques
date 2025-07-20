input_tensor = torch.randn(1, 3, 5)
pooling_layer = torch.nn.LPPool1d(norm_type=2, kernel_size=3)
output_tensor = pooling_layer(input_tensor)