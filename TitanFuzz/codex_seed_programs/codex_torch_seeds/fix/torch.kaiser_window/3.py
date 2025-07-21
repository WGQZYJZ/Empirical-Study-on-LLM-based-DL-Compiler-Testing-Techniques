'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kaiser_window\ntorch.kaiser_window(window_length, periodic=True, beta=12.0, *, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
window_length = 100
beta = 12.0
kaiser_window = torch.kaiser_window(window_length, periodic=True, beta=beta)
print('Kaiser window:')
print(kaiser_window)
print('Kaiser window shape: ', kaiser_window.shape)