x = torch.rand(1, 3, 3)
y = torch.nn.Softshrink(lambd=0.5)(x)