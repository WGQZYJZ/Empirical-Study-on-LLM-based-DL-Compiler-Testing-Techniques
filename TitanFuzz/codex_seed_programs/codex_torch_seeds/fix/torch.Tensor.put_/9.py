'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
index = torch.tensor([0, 1, 2])
source = torch.tensor([1, 2, 3])
print(input_tensor)
torch.Tensor.put_(input_tensor, index, source, accumulate=False)
print(input_tensor)