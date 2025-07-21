'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nelement\ntorch.Tensor.nelement(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_tensor.nelement() =', input_tensor.nelement())
input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('input_tensor.nelement() =', input_tensor.nelement())
input_tensor = torch.tensor([[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]], [[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]])
print('input_tensor.nelement() =', input_tensor.nelement())