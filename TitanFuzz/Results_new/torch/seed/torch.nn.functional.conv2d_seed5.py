input_data = torch.randn(1, 1, 3, 3)
conv_output = torch.nn.functional.conv2d(input_data, input_data)