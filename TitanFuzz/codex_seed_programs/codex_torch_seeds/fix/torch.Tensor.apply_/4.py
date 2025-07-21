'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.apply_\ntorch.Tensor.apply_(_input_tensor, callable)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(3, 3))
print('Input Tensor: ', _input_tensor)
_output_tensor = _input_tensor.apply_((lambda x: (x * 2)))
print('Output Tensor: ', _output_tensor)