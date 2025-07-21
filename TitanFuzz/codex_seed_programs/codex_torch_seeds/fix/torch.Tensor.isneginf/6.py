'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isneginf\ntorch.Tensor.isneginf(_input_tensor)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.Tensor.isneginf')
input_tensor = torch.tensor([(- 1), (- 2), (- 3), 0, 1, 2, 3])
output_tensor = input_tensor.isneginf()
print('The output tensor is: ', output_tensor)