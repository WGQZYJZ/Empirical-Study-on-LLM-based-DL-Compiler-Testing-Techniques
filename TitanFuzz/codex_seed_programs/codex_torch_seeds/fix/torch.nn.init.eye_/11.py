'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
if True:
    input_tensor = torch.rand(3, 3)
    print('Input tensor: ', input_tensor)
    torch.nn.init.eye_(input_tensor)
    print('Output tensor: ', input_tensor)