'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.normal_\ntorch.Tensor.normal_(_input_tensor, mean=0, std=1, *, generator=None)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.normal_(input_tensor)
print(input_tensor)
torch.Tensor.normal_(input_tensor, mean=1)
print(input_tensor)
torch.Tensor.normal_(input_tensor, std=2)
print(input_tensor)
torch.Tensor.normal_(input_tensor, mean=1, std=2)
print(input_tensor)