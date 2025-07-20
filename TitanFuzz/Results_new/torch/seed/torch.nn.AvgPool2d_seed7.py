input = torch.randn(1, 1, 4, 4)
avgpool2d = torch.nn.AvgPool2d(2, stride=1, padding=0)
output = avgpool2d(input)