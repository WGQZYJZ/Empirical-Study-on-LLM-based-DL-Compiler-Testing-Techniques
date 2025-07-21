'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [1, 2, 1, 2, 1]])
_output_tensor = _input_tensor.cummax(dim=1)
print('The input tensor is:\n', _input_tensor)
print('The output tensor is:\n', _output_tensor)