'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.imag\ntorch.imag(input)\n'
import torch
input_data = torch.tensor([(1 + 2j), (2 + 5j), (1 + 1j)])
print('Input data: ', input_data)
imag_part = torch.imag(input_data)
print('Imaginary part: ', imag_part)