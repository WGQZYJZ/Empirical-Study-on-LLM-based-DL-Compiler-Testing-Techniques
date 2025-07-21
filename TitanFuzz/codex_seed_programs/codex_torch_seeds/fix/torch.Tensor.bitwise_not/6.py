'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([1, 0, 0, 0, 1, 1, 0, 1], dtype=torch.uint8)
_output_tensor = torch.Tensor.bitwise_not(_input_tensor)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)