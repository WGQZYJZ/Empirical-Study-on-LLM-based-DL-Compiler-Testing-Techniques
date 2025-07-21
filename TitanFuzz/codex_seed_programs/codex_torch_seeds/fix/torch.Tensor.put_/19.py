'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.rand(5, 3)
index = torch.tensor([[4, 3, 1], [3, 1, 2]])
source = torch.tensor([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])
input_tensor.put_(index, source)
print(input_tensor)