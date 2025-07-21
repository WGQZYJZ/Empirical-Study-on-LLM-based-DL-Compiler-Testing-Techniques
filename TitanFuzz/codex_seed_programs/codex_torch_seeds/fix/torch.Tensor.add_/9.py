'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
print(tensor_a.add_(tensor_b))
print(tensor_a)
'\nTask 4: Call the API torch.Tensor.add\ntorch.Tensor.add(input, other, *, alpha=1)\n'
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
print(tensor_a.add(tensor_b))
print(tensor_a)