input = torch.randn(1, 1, 4, 4)
avg_pool2d = torch.nn.functional.avg_pool2d(input, kernel_size=2, stride=2, padding=0)