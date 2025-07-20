n_fft = 20
win_length = 10
hop_length = 5
window = torch.ones(win_length)
center = True
normalized = False
onesided = None
length = None
return_complex = False
x = torch.randn(1, 1, n_fft)
torch.Tensor.istft(x, n_fft, hop_length, win_length, window, center, normalized, onesided, length, return_complex)