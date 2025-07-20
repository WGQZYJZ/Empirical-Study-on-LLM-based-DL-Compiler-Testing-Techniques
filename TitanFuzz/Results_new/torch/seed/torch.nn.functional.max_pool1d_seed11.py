input = torch.randn(1, 1, 4)
output = torch.nn.functional.max_pool1d(input, kernel_size=2, stride=2, padding=0)