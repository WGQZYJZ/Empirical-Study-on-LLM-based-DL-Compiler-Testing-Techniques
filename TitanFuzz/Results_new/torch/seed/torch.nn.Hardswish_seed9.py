input = Variable(torch.randn(1, 3, 3, 3))
output = torch.nn.Hardswish(inplace=False)(input)