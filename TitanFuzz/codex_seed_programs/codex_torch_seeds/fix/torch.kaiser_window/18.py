'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.kaiser_window\ntorch.kaiser_window(window_length, periodic=True, beta=12.0, *, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
import numpy as np
print('Task 3: Call the API torch.kaiser_window')
window_length = 5
periodic = True
beta = 12.0
window = torch.kaiser_window(window_length, periodic=periodic, beta=beta)
print('window: ', window)
window_np = np.kaiser(window_length, beta)
print('window_np: ', window_np)