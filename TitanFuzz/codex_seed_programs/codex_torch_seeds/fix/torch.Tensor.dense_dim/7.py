'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dense_dim\ntorch.Tensor.dense_dim(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
_output_tensor = _input_tensor.dense_dim(1, 2, 3)
print('_input_tensor: ', _input_tensor)
print('_output_tensor: ', _output_tensor)