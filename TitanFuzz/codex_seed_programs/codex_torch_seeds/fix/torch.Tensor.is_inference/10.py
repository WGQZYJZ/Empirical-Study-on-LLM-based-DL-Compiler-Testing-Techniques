'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_inference\ntorch.Tensor.is_inference(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
is_inference = input_tensor.is_inference()
print(is_inference)