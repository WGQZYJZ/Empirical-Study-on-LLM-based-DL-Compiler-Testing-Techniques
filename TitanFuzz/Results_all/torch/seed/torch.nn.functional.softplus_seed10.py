input = torch.randn(2, 3, requires_grad=True)
output = torch.nn.functional.softplus(input)