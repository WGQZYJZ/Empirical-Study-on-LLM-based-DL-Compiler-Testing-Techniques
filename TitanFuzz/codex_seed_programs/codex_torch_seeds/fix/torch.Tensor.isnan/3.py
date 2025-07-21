'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isnan\ntorch.Tensor.isnan(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 4)
_input_tensor[(1, 1)] = float('nan')
_output_tensor = torch.Tensor.isnan(_input_tensor)
print(_output_tensor)
print(torch.tensor([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
print(torch.tensor([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))