x = torch.tensor([[(- 0.5), 0.5, 1.0], [1.0, (- 0.5), 0.5]])
y = torch.clip(x, min=(- 0.4), max=0.6)