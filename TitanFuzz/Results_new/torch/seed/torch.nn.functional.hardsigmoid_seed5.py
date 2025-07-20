input = Variable(torch.randn(4, 4))
output = torch.nn.functional.hardsigmoid(input)