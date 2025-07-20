x = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0], dtype=torch.float)
y = torch.special.expit(x)
x = torch.tensor([[(- 2.0), (- 1.0), 0.0, 1.0, 2.0], [(- 2.0), (- 1.0), 0.0, 1.0, 2.0]], dtype=torch.float)
y = torch.special.expit(x)