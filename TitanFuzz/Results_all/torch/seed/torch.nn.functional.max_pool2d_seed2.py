input = torch.randn(1, 1, 4, 4)
output = torch.nn.functional.max_pool2d(input, kernel_size=2, stride=2)
output = torch.nn.functional.max_pool2d(input, kernel_size=2, stride=2, padding=1)
output = torch.nn.functional.max_pool2d(input, kernel_size=2, stride=2, dilation=2)