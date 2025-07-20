input = Variable(torch.randn(1, 1))
output = torch.nn.functional.elu(input)