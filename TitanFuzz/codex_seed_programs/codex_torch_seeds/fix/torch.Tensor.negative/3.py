'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_output_tensor = torch.Tensor.negative(_input_tensor)
print('input tensor: {}'.format(_input_tensor))
print('output tensor: {}'.format(_output_tensor))