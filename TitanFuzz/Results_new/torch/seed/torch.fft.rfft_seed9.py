a = np.random.randn(1, 4, 4)
a = torch.tensor(a, dtype=torch.float64)
b = torch.fft.rfft(a, n=None, dim=(- 1), norm=None, out=None)