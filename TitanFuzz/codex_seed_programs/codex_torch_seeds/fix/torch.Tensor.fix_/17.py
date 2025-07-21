'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix_\ntorch.Tensor.fix_(_input_tensor)\n'
import torch
_input_tensor = torch.randint(0, 10, (3, 3))
print(_input_tensor)
torch.Tensor.fix_(_input_tensor)
print(_input_tensor)