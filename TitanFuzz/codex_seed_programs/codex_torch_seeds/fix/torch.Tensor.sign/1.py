'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 3)
output_tensor = torch.Tensor.sign(_input_tensor)
print(output_tensor)