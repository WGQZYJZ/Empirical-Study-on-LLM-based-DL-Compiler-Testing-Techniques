'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
trunc_data = input_data.trunc()
print(trunc_data)