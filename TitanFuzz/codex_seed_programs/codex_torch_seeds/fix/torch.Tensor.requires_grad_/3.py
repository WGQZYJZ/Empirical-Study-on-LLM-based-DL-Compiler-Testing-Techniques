'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.requires_grad_\ntorch.Tensor.requires_grad_(_input_tensor, requires_grad=True)\n'
import torch
X = torch.Tensor([[1, 2], [3, 4]])
Y = torch.Tensor([[5, 6], [7, 8]])
X.requires_grad_(True)
Y.requires_grad_(True)
print(X.requires_grad)
print(Y.requires_grad)