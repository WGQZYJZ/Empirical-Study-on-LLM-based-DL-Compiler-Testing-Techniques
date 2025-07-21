'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([[0, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 1]])
_output_tensor = torch.Tensor.bitwise_not_(_input_tensor)
print(_output_tensor)