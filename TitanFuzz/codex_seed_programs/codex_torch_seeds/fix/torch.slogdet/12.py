'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor:\n', input_tensor)
(sign, log_abs_det) = torch.slogdet(input_tensor)
print('Sign:', sign)
print('Log Absolute Determinant:', log_abs_det)