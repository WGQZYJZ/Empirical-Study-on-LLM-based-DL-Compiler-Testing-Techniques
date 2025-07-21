'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flipud\ntorch.Tensor.flipud(_input_tensor)\n'
import torch
import torch
_input_tensor = torch.tensor([[0.5, 0.5, 0.5], [1, 1, 1], [2, 2, 2]])
_output_tensor = torch.Tensor.flipud(_input_tensor)
print('Input tensor:\n{}'.format(_input_tensor))
print('Output tensor:\n{}'.format(_output_tensor))