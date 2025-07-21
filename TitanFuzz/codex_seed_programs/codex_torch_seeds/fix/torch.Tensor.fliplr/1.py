'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fliplr\ntorch.Tensor.fliplr(_input_tensor)\n'
import torch
_input_tensor = torch.rand(4, 4)
print('Input: ', _input_tensor)
_flipped_tensor = torch.Tensor.fliplr(_input_tensor)
print('Flipped: ', _flipped_tensor)