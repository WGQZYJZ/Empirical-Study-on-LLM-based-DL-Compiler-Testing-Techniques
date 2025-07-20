input = torch.randn(3, 3, requires_grad=True)
output = torch.pinverse(input)