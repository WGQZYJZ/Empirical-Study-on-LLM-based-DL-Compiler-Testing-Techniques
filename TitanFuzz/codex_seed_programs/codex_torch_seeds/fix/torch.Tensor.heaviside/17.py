'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(torch.Tensor.heaviside(input_data, 0.5))