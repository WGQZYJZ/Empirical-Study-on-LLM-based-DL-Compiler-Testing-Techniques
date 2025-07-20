input = torch.randn(1, 1, 3, 3)
weight = torch.randn(1, 1, 2, 2)
output = torch.nn.functional.conv2d(input, weight)
output = torch.nn.functional.conv2d(input, weight, stride=2, padding=1)