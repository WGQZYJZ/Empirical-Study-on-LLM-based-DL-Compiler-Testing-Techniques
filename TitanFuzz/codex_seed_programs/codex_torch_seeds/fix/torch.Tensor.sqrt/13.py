'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt\ntorch.Tensor.sqrt(_input_tensor)\n'
import torch
if True:
    input_tensor = torch.randn(1, 3)
    output_tensor = torch.Tensor.sqrt(input_tensor)
    print('Input tensor: {}'.format(input_tensor))
    print('Output tensor: {}'.format(output_tensor))