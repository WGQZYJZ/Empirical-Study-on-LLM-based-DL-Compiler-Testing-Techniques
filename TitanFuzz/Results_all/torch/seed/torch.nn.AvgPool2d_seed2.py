input = Variable(torch.randn(1, 1, 8, 8))
avg_pool = torch.nn.AvgPool2d(2, stride=2)
output = avg_pool(input)