'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_inference\ntorch.Tensor.is_inference(_input_tensor)\n'
import torch
_input_tensor = torch.rand(10, 10)
print(torch.Tensor.is_inference(_input_tensor))