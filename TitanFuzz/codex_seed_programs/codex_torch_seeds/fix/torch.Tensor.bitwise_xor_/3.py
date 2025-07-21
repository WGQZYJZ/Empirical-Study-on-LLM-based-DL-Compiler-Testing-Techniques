'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
_other = torch.tensor([[1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 0, 0]])
torch.Tensor.bitwise_xor_(_input_tensor, _other)
print(_input_tensor)