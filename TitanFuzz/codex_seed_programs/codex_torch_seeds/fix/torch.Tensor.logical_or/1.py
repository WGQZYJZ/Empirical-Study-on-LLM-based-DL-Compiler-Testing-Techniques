'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_or\ntorch.Tensor.logical_or(_input_tensor, other)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(2, 3), dtype=torch.int32)
other = torch.randint(low=0, high=2, size=(2, 3), dtype=torch.int32)
_output_tensor = torch.Tensor.logical_or(_input_tensor, other)
print('input tensor: {}'.format(_input_tensor))
print('other tensor: {}'.format(other))
print('output tensor: {}'.format(_output_tensor))