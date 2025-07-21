'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
vec = torch.tensor([1, 2, 3])
'\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
result = torch.Tensor.mv(input_tensor, vec)
print(result)