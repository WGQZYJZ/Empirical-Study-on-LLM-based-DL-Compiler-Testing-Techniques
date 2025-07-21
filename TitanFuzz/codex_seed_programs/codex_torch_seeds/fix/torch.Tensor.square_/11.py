'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square_\ntorch.Tensor.square_(_input_tensor)\n'
import torch
input_data = torch.arange(9, dtype=torch.float32)
input_data = input_data.view(3, 3)
print(torch.Tensor.square_(input_data))