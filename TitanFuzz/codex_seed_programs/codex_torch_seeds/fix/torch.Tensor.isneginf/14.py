'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_tensor = torch.tensor([(- float('inf')), (- 3.0), 0.0, 2.0, float('inf')])
'\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
output_tensor = input_tensor.isneginf()
print('input tensor:\n', input_tensor)
print('output tensor:\n', output_tensor)