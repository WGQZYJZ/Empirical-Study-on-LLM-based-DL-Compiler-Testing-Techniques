input = torch.randn(20, 16, 50, 32)
output = torch.nn.functional.avg_pool2d(input, kernel_size=5, stride=1, padding=2)