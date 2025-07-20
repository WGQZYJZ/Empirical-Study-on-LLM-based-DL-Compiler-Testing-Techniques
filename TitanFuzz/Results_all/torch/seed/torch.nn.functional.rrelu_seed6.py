input = Variable(torch.randn(1, 2, 3, 4))
output = torch.nn.functional.rrelu(input)