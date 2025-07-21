'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
_input_tensor = torch.tensor([1, 2, 3, 4])
_output_tensor = _input_tensor.broadcast_to([4, 4])
print('The original tensor: {}'.format(_input_tensor))
print('The broadcasted tensor: {}'.format(_output_tensor))