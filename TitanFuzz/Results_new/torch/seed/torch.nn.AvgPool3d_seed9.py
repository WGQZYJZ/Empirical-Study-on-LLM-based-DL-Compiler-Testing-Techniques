input = Variable(torch.randn(1, 1, 5, 5, 5))
avg_pool = torch.nn.AvgPool3d(kernel_size=2, stride=2)
output = avg_pool(input)