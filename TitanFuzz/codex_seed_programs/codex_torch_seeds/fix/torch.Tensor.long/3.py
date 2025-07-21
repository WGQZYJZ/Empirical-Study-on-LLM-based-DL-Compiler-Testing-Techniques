'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(low=0, high=4, size=(3, 3))
print('Input data: \n', _input_tensor)
_output_tensor = torch.Tensor.long(_input_tensor)
print('Output data: \n', _output_tensor)