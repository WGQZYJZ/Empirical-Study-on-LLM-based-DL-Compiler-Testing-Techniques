'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfft2\ntorch.fft.irfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import numpy as np
input_data = torch.rand(2, 3, 4, 5)
output = torch.fft.irfft2(input_data)
print('input_data:\n', input_data)
print('output:\n', output)
np_input_data = input_data.numpy()
np_output = np.fft.irfft2(np_input_data)
print('np_input_data:\n', np_input_data)
print('np_output:\n', np_output)
torch_input_data = torch.tensor(np_input_data)
torch_output = torch.fft.irfft2(torch_input_data)