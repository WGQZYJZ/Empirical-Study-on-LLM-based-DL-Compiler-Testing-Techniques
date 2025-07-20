N = 1024
T = (1.0 / 800.0)
x = np.linspace(0.0, (N * T), N)
y = (np.sin((((50.0 * 2.0) * np.pi) * x)) + (0.5 * np.sin((((80.0 * 2.0) * np.pi) * x))))
X = torch.tensor(y, dtype=torch.float32)
freq = torch.fft.fftfreq(N, d=T)
X_fft = torch.fft.fft(X)
X_fft_mag = torch.abs(X_fft)
X_fft_mag_db = (20 * torch.log10(X_fft_mag))