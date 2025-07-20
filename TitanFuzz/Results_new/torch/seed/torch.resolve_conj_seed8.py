input = torch.randn(4, 4, requires_grad=True)
output = torch.resolve_conj(input)
output.backward(torch.ones(4, 4))