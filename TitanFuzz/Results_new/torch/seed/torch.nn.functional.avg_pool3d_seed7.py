input = torch.randn(1, 1, 5, 5, 5)
output = torch.nn.functional.avg_pool3d(input, kernel_size=3, stride=2, padding=1)