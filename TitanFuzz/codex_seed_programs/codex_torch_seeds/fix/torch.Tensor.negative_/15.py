'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative_\ntorch.Tensor.negative_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]], dtype=torch.float32)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.negative_(input_tensor)
print('Output tensor: ', output_tensor)