input_data = torch.randn(1, 1, 3, 3)
torch.set_num_threads(8)
output_data = torch.nn.functional.conv2d(input_data, input_data)