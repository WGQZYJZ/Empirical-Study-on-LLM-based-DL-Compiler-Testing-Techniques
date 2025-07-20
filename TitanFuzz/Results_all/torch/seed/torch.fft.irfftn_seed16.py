N = 16
x = torch.randn(N, N, N)
y = torch.fft.irfftn(x)