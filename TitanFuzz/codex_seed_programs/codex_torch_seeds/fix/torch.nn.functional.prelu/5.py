'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
import torch.nn.functional as F
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
weight = torch.Tensor([0.3])
output = F.prelu(input_data, weight)
print(output)