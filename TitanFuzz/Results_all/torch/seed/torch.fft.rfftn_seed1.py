x = np.random.randn(3, 4, 5)
x = torch.from_numpy(x)
y = torch.fft.rfftn(x, s=None, dim=None, norm=None, out=None)