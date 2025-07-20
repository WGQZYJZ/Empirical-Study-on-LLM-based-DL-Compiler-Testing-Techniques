input = Variable(torch.randn(1, 64, 8, 8, 8))
output = torch.nn.AdaptiveAvgPool3d((1, 1, 1))(input)