'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinc\ntorch.Tensor.sinc(_input_tensor)\n'
import torch
input_data = torch.randn(4, 4)
print(input_data)
result = torch.Tensor.sinc(input_data)
print(result)