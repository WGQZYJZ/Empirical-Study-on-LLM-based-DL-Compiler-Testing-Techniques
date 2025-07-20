x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.softsign(x)