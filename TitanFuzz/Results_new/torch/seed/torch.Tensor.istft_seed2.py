input_tensor = torch.randn(5, 5)
torch.Tensor.istft(input_tensor, n_fft=5, hop_length=5, win_length=5, window=None, center=True, normalized=False, onesided=None, length=None, return_complex=False)