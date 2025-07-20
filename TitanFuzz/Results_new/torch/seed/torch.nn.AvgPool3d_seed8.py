input = Variable(torch.randn(1, 1, 3, 3, 3))
pool = torch.nn.AvgPool3d(kernel_size=2, stride=2, padding=1)
output = pool(input)