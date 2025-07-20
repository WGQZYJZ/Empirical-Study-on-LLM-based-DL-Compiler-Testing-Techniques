input = Variable(torch.randn(1, 1, 4, 4))
output = torch.nn.functional.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)