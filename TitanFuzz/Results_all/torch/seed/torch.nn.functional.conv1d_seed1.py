input = torch.randn(1, 1, 5)
weight = torch.randn(1, 1, 3)
output = torch.nn.functional.conv1d(input, weight, padding=1)
input = torch.randn(1, 1, 5, 5)
weight = torch.randn(1, 1, 3, 3)
output = torch.nn.functional