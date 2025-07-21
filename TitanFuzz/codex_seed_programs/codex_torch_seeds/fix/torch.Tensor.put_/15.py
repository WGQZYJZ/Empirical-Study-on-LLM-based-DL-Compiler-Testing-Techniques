'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
index = torch.tensor([[0, 1], [1, 2]])
source = torch.tensor([3, 4])
input_tensor.put_(index, source, accumulate=False)
print(input_tensor)