'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
_input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.int16)
print('Input:', _input_tensor)
torch.Tensor.bitwise_not_(_input_tensor)
print('Output:', _input_tensor)