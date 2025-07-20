input = torch.randn(1, 2, 3, requires_grad=True)
output = torch.nn.functional.softshrink(input)