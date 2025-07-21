'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
'Task 1: import PyTorch'
'Task 2: Generate input data'
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor: ', _input_tensor)
'Task 3: Call the API torch.Tensor.msort'
_output_tensor = torch.Tensor.msort(_input_tensor)
print('Output tensor: ', _output_tensor)