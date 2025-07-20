input = torch.randn(1, 1, 3, 3)
torch.nn.functional.softshrink(input, lambd=0.5)
input = torch.randn(1, 1, 3, 3)
torch.nn.functional.softsign(input)