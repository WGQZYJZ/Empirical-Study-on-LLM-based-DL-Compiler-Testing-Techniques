'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
import torch
_input_tensor = torch.tensor([1, 2, 3, 4, 5])
_output_tensor = torch.Tensor.tile(_input_tensor, dims=2)
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)