input = Variable(torch.randn(1, 1, 4, 4))
pool = torch.nn.AvgPool2d(kernel_size=2, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)
output = pool(input)