"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.stft\ntorch.stft(input, n_fft, hop_length=None, win_length=None, window=None, center=True, pad_mode='reflect', normalized=False, onesided=None, return_complex=None)\n"
import torch
input = torch.randn(1, 10)
print(input.shape)
n_fft = 4
stft_out = torch.stft(input, n_fft)
print(stft_out.shape)
print(stft_out)