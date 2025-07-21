'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.is_signed())