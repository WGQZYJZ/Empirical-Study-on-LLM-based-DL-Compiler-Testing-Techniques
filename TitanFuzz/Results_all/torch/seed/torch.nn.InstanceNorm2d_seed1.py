input = torch.randn(1, 3, 5, 5)
output = torch.nn.InstanceNorm2d(3)(input)