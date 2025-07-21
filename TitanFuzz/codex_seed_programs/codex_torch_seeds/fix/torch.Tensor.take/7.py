'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
input_tensor = torch.rand(4, 3)
print(input_tensor.take(torch.tensor([0, 2])))