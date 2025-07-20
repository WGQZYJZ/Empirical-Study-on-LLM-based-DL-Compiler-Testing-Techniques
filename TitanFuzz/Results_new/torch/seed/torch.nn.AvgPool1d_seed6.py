input = Variable(torch.randn(1, 1, 5))
output = torch.nn.AvgPool1d(3, stride=1, padding=0, ceil_mode=False, count_include_pad=True)(input)