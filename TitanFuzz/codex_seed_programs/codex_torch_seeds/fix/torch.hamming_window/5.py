'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hamming_window\ntorch.hamming_window(window_length, periodic=True, alpha=0.54, beta=0.46, *, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
window_length = 10
input_data = torch.randn(window_length)
output = torch.hamming_window(window_length)
print('input_data: ', input_data)
print('output: ', output)