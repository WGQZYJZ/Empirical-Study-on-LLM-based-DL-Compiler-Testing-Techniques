'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(5,))
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_input_tensor.int_repr()))