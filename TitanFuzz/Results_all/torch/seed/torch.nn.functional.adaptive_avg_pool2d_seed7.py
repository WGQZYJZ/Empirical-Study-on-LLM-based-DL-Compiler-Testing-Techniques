input_data = torch.rand(1, 1, 4, 4)
output_size = (1, 1)
torch.nn.functional.adaptive_avg_pool2d(input_data, output_size)