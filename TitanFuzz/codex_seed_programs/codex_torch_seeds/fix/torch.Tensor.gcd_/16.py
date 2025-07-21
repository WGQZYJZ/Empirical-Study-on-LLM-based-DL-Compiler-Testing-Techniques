'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_data = torch.tensor([[10, 15, 20], [25, 30, 35]])
torch.Tensor.gcd_(input_data, 5)
print('input data = \n', input_data)