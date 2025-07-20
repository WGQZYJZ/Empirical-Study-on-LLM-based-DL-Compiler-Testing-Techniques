input = Variable(torch.randn(1, 1, 4, 4, 4))
avg_pool = torch.nn.AdaptiveAvgPool3d(output_size=(2, 2, 2))
avg_pool(input)