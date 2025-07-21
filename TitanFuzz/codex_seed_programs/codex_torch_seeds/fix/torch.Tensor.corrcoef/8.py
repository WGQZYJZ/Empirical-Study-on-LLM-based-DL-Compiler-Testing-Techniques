'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.corrcoef\ntorch.Tensor.corrcoef(_input_tensor)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
print(torch.Tensor.corrcoef(input_data))