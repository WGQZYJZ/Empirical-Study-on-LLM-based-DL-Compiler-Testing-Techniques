'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(20, 20)
output_tensor = input_tensor.digamma()
print(output_tensor)