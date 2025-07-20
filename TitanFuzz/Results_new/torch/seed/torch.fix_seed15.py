x = torch.tensor([(- 1.8), (- 1.2), (- 0.4), 0.4, 1.2, 1.8], dtype=torch.float32)
y = torch.fix(x)
x = torch.tensor([(- 1.8), (- 1.2), (- 0.4), 0.4, 1.2, 1.8], dtype=torch.float32)
y = torch.fix(x, out=torch.empty_like(x))