'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
print(input_data)
torch.Tensor.requires_grad_(input_data, requires_grad=True)
print(input_data)