input_data = torch.randn(20, 16, 50, 32, 45)
max_pool_3d = torch.nn.MaxPool3d(kernel_size=3, stride=2)
output = max_pool_3d(input_data)