input = torch.randn(20, 16, 50, 32, 45)
output = torch.nn.AvgPool3d(kernel_size=3, stride=2, padding=1)(input)