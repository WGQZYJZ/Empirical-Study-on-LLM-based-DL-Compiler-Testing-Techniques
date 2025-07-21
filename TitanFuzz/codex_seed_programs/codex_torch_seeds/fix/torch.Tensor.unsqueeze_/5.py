'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze_\ntorch.Tensor.unsqueeze_(_input_tensor, dim)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x_unsqueeze = x.unsqueeze_(0)
print('x_unsqueeze = ', x_unsqueeze)
x_unsqueeze = x.unsqueeze_(1)
print('x_unsqueeze = ', x_unsqueeze)