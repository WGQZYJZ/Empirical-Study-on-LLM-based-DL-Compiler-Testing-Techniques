'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.polygamma\ntorch.Tensor.polygamma(_input_tensor, n)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.polygamma(input_tensor, 3)
print(output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pow\ntorch.Tensor.pow(_input_tensor, exponent)\n'
import torch
import numpy as np
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.pow(input_tensor, 3)
print(output_tensor)