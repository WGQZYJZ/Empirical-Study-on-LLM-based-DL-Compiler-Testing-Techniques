'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input tensor: {}'.format(input_tensor))
print('Output tensor: {}'.format(torch.Tensor.is_conj(input_tensor)))