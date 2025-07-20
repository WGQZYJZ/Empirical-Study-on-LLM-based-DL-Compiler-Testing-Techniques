input = torch.randn(1, 1, 5, 5, 5)
output = torch.nn.functional.max_pool3d(input, kernel_size=3, stride=2, padding=1)