'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfinv_\ntorch.Tensor.erfinv_(_input_tensor)\n'
import torch
data = torch.randn(100, 100)
result = torch.Tensor.erfinv_(data)
print(result)