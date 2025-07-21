'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not\ntorch.Tensor.logical_not(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
_output_tensor = torch.Tensor.logical_not(_input_tensor)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)