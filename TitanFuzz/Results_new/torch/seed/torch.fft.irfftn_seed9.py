x = np.random.rand(2, 3, 4, 5)
x = torch.tensor(x, dtype=torch.float32)
y = torch.fft.irfftn(x, s=None, dim=None, norm=None, out=None)