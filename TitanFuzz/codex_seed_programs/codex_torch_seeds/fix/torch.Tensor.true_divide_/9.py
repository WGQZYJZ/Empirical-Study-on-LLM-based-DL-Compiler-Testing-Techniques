'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.true_divide_\ntorch.Tensor.true_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.arange(9, dtype=torch.float32)
print(input_tensor)
input_tensor.true_divide_(3)
print(input_tensor)