'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.istft\ntorch.Tensor.istft(_input_tensor, n_fft, hop_length=None, win_length=None, window=None, center=True, normalized=False, onesided=None, length=None, return_complex=False)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
torch.Tensor.istft(input_tensor, n_fft=10, hop_length=2)