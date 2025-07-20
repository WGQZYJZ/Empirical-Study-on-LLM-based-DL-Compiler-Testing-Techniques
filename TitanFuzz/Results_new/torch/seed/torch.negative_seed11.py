input = torch.randn(3, requires_grad=True)
output = torch.negative(input)
output.backward(torch.ones(input.size()))