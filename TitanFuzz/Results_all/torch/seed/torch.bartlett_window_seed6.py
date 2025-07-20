data = np.arange(0, 100, 0.1)
data = torch.tensor(data)
window = torch.bartlett_window(100)