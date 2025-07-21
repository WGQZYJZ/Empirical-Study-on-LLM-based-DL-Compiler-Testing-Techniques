'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.tensor([[0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 0, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1]])
_output_tensor = _input_tensor.count_nonzero(dim=None)
print('output tensor: ', _output_tensor)