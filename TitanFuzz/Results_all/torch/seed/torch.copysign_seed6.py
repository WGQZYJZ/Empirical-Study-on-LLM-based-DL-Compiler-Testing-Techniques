x = torch.tensor([(- 1.0), 2.0, (- 3.0), 4.0])
y = torch.tensor([1.0, (- 2.0), 3.0, (- 4.0)])
z = torch.copysign(x, y)