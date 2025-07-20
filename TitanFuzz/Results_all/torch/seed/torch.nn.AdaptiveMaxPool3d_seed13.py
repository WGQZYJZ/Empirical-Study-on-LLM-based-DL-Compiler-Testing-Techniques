input = Variable(torch.randn(1, 1, 32, 32, 32))
output = torch.nn.AdaptiveMaxPool3d((4, 4, 4))(input)