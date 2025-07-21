'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10_\ntorch.Tensor.log10_(_input_tensor)\n'
import torch
_input_tensor = torch.randint(10, (2, 3, 4), dtype=torch.float32)
print('Input tensor: ', _input_tensor)
torch.Tensor.log10_(_input_tensor)
print('Output tensor: ', _input_tensor)