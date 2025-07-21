'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.data_ptr\ntorch.Tensor.data_ptr(_input_tensor)\n'
import torch
import torch
_input_tensor = torch.rand(2, 3)
print('_input_tensor: ', _input_tensor)
_output_tensor = torch.Tensor.data_ptr(_input_tensor)
print('_output_tensor: ', _output_tensor)