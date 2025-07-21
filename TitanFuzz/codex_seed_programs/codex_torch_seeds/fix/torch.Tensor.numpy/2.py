'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.randn(5, 3)
print(_input_tensor)
output_tensor = _input_tensor.numpy()
print(output_tensor)