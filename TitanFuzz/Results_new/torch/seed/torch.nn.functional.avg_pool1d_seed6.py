input = Variable(torch.randn(1, 1, 3))
output = torch.nn.functional.avg_pool1d(input, kernel_size=2, stride=1, padding=0)