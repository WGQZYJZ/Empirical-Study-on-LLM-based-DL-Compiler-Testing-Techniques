'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
tensor = torch.randn(5, 3)
print(tensor)
result = tensor.dsplit(1)
print(result)