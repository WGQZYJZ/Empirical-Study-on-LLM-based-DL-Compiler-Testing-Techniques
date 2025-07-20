x = torch.rand(4, 2, 8)
y = torch.fft.fft(x, 2, 1)
x_np = x.numpy()
y_np = np.fft.fft(x_np, 2, 1)