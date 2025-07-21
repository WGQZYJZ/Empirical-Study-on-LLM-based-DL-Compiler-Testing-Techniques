'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input Tensor is: ', input_tensor)
q = torch.Tensor([0.5])
output_tensor = input_tensor.quantile(q)
print('Output Tensor is: ', output_tensor)