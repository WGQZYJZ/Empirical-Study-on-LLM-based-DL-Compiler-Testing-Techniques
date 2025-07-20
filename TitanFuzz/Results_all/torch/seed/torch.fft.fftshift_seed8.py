x = torch.arange(0, 16).reshape(4, 4)
y = torch.fft.fftshift(x)
x_np = np.arange(0, 16).reshape(4, 4)
y_np = np.fft.fftshift(x_np)