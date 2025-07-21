'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
_input_tensor = torch.randint(1, 10, (2, 3, 4))
print('Input tensor:\n{}'.format(_input_tensor))
shifts = torch.tensor([1, 2])
dims = torch.tensor([0, 1])
output_tensor = torch.Tensor.roll(_input_tensor, shifts, dims)
print('Output tensor:\n{}'.format(output_tensor))