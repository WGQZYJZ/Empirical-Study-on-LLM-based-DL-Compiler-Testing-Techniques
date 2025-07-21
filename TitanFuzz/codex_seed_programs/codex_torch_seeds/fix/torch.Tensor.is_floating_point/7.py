'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.is_floating_point()
print('The result of torch.Tensor.is_floating_point is: ', _output_tensor)