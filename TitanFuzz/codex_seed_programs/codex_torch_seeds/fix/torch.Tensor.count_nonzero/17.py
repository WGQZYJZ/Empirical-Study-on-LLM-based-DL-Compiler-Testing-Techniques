'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.tensor([[1, 0, 0, 1, 1], [0, 0, 1, 0, 1]])
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('The output tensor is: ', _output_tensor)