'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinc\ntorch.Tensor.sinc(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor)
sinc_output = torch.Tensor.sinc(_input_tensor)
print(sinc_output)