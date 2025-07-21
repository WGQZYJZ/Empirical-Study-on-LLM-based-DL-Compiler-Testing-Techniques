'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
_input_tensor = torch.rand(2, 3)
_flipped_tensor = torch.Tensor.flip(_input_tensor, (1,))
print(_flipped_tensor)