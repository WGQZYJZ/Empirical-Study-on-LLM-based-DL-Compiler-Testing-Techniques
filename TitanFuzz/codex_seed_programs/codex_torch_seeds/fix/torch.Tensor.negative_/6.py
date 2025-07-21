'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
_input_tensor = torch.randint(low=0, high=100, size=(2, 3))
print(_input_tensor)
print(_input_tensor.negative_())
print(_input_tensor.negative())