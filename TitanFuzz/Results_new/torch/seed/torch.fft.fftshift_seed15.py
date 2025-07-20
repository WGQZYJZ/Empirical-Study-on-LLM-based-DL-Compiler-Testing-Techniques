x = torch.randn(4, 4, 4)
y = torch.fft.fftshift(x, dim=0)
a = np.fft.fftshift(x.numpy(), axes=0)