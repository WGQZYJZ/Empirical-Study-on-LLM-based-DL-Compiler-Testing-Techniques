input_data = torch.arange(0, 27).view(1, 1, 3, 3, 3)
input_data = input_data.float()
output = torch.nn.functional.max_pool3d(input_data, kernel_size=2, stride=2)