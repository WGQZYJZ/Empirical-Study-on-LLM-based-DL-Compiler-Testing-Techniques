'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(2, 3, 4, 5), dtype=torch.int32)
output_tensor = torch.Tensor.bool(_input_tensor)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(output_tensor)