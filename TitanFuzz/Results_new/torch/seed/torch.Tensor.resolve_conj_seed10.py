input = Variable(torch.randn(3, 1, 3, 3))
output = torch.Tensor.resolve_conj(input)