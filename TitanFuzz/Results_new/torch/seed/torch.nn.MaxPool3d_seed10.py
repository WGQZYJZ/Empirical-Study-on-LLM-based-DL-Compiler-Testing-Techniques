input_data = torch.randn(1, 1, 5, 5, 5)
max_pool_3d = torch.nn.MaxPool3d(kernel_size=2, stride=1)
output = max_pool_3d(input_data)