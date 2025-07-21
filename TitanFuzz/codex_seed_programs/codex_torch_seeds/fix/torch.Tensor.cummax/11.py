'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 4))
print('Input tensor: ', input_tensor)
print('Cummax of input tensor: ', input_tensor.cummax(dim=0))