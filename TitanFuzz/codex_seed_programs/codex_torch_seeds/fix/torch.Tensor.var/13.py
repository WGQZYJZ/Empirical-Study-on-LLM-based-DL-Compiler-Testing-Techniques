'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.var\ntorch.Tensor.var(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('input_tensor: ', input_tensor)
output_tensor = input_tensor.var(dim=0, unbiased=True, keepdim=False)
print('output_tensor: ', output_tensor)