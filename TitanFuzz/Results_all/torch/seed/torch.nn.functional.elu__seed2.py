x = torch.tensor([(- 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
y = torch.nn.functional.elu_(x, alpha=1.0)