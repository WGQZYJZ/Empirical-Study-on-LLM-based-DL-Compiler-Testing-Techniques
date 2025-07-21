'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.rand(3, 3)
index = torch.tensor([[0, 1, 2], [1, 1, 1]])
source = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
input_tensor.put_(index, source, accumulate=False)
print(input_tensor)
input_tensor.put_(index, source, accumulate=True)
print(input_tensor)