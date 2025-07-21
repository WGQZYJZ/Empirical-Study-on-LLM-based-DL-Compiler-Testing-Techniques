'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_inference\ntorch.Tensor.is_inference(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(1, 1, 1, 1)
is_inference = torch.Tensor.is_inference(input_tensor)
print(is_inference)