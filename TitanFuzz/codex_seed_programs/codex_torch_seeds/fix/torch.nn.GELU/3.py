'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GELU\ntorch.nn.GELU()\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
gelu = torch.nn.GELU()
output = gelu(input_data)
print(output)