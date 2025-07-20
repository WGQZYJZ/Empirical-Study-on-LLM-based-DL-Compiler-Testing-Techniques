x = torch.tensor([(- 1.0), 1.0, (- 0.5), 0.5])
y = torch.clip(x, (- 0.5), 0.5)