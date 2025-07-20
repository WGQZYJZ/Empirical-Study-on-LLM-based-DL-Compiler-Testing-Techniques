input = torch.randn(1, 3, 4, 4)
output = torch.nn.functional.softshrink(input, lambd=0.5)