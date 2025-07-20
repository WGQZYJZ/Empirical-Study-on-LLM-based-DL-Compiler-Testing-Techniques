input_data = torch.randn(1, 1, 4, 4, 4)
avg_pool3d = torch.nn.AvgPool3d(kernel_size=2, stride=2)
output = avg_pool3d(input_data)