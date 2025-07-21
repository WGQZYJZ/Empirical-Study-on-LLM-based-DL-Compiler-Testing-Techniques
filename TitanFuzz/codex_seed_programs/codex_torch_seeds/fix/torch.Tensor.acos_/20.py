'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acos_\ntorch.Tensor.acos_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.0), 0.0, 1.0])
torch.Tensor.acos_(input_tensor)
print('input_tensor = ', input_tensor)
'\nExpected output:\ninput_tensor =  tensor([3.1416, 1.5708, 0.0000])\n'