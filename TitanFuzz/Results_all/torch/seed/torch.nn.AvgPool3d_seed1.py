input_data = torch.randn(4, 16, 5, 5, 5)
avg_pool3d = torch.nn.AvgPool3d(kernel_size=3, stride=2, padding=1)
output = avg_pool3d(input_data)