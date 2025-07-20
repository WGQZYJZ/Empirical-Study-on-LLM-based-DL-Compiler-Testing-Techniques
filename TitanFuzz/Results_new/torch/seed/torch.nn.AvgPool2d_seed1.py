input = torch.randn(1, 1, 4, 4)
pool = torch.nn.AvgPool2d(2, stride=2)
output = pool(input)