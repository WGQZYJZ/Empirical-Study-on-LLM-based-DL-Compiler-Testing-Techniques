data = np.arange(10)
result = torch.bartlett_window(10)
result = torch.bartlett_window(10, periodic=False)
result = torch.bartlett_window(10, periodic=False, dtype=torch.float32)