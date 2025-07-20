input = torch.randn(1, 1, 4, 4)
avgpool = torch.nn.AdaptiveAvgPool2d((1, 1))
output = avgpool(input)