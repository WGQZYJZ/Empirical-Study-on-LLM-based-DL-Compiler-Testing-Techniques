input = torch.randn(1, 1, 5)
weight = torch.randn(1, 1, 3)
output = torch.nn.functional.conv1d(input, weight, stride=1, padding=0)