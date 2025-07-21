'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.quantile\ntorch.Tensor.quantile(_input_tensor, q, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input tensor: ', input_tensor)
quantile_value = input_tensor.quantile(q=0.5, dim=1, keepdim=True)
print('Quantile value: ', quantile_value)