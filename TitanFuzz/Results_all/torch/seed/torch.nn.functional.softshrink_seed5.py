x = torch.tensor(np.arange((- 5), 5, 0.1), dtype=torch.float32)
y = torch.nn.functional.softshrink(x, lambd=0.5)