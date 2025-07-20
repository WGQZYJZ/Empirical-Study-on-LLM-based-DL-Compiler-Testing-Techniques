input_data = torch.randn(1, 1, 5, 5)
output_data = torch.nn.functional.conv2d(input_data, input_data, padding=1)
input_data = torch.randn(1, 1, 5, 5)
output_data