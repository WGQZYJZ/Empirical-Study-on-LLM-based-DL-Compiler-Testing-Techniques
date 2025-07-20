input = torch.randn(1, 3, 5, 5)
output = torch.nn.functional.softshrink(input, lambd=0.5)