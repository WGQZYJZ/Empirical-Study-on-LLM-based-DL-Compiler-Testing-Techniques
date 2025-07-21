'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh\ntorch.Tensor.arccosh(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_tensor = torch.Tensor.arccosh(input_tensor)
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)