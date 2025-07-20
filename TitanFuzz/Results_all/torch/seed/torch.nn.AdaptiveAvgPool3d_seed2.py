x = Variable(torch.randn(1, 3, 10, 10, 10))
y = torch.nn.AdaptiveAvgPool3d(output_size=1)(x)