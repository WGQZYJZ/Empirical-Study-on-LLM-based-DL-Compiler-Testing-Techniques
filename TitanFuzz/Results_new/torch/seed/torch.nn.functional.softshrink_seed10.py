x = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
y = torch.nn.functional.softshrink(x, lambd=0.5)