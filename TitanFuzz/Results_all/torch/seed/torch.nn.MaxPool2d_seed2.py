input_data = torch.randn(1, 1, 7, 7)
max_pool_2d = torch.nn.MaxPool2d(kernel_size=2, stride=2)
output_data = max_pool_2d(input_data)