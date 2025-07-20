input = Variable(torch.randn(10, 10))
output = torch.nn.functional.mish(input)