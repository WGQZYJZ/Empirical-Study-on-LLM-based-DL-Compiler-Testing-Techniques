'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(_input_tensor, *shape)\n'
import torch
'\nTask 1:\n'
'\nTask 2:\n'
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
'\nTask 3:\n'
_reshaped_tensor = _input_tensor.reshape(3, 2)
print('Input Tensor: \n', _input_tensor)
print('Reshaped Tensor: \n', _reshaped_tensor)