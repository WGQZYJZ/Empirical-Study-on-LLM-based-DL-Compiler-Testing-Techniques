input = torch.randn(3, 5, requires_grad=True)
output = torch.nn.functional.tanh(input)