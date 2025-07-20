input = torch.randn(1, 10)
n_fft = 4
stft_out = torch.stft(input, n_fft)