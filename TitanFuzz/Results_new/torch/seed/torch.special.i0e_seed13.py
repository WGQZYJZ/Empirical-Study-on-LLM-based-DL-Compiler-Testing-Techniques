x = torch.tensor([(- 2), (- 1), 0, 1, 2])
y = torch.special.i0e(x)
y_np = y.numpy()
y_torch = torch.from_numpy(y_np)