'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
_input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
mat2 = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
print('The result of _input_tensor.mm(mat2) is: {}'.format(_input_tensor.mm(mat2)))