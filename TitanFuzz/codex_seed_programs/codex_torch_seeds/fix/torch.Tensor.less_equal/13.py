'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_equal\ntorch.Tensor.less_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(2, 3)
result = torch.Tensor.less_equal(input_tensor, 0)
print(result)