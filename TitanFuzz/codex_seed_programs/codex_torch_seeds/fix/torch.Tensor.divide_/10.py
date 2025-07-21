'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.divide_\ntorch.Tensor.divide_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
tensor_a = torch.tensor([1, 2, 3, 4, 5])
tensor_b = torch.tensor([2, 2, 2, 2, 2])
print(tensor_a.divide_(tensor_b))
print(tensor_a.divide_(2))
print(tensor_a.divide_(2, rounding_mode='floor'))