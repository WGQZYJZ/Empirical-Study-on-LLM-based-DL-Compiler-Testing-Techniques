input = Variable(torch.randn(3))
output = torch.nn.functional.softplus(input)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)