'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
input_tensor = torch.Tensor(3, 4)
torch.Tensor.fill_(input_tensor, 1.0)
print(input_tensor)