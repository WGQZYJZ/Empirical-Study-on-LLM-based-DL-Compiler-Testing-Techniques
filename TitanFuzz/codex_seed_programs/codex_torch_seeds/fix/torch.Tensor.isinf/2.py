'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[float('inf'), (- float('inf')), float('nan')]])
print('Input tensor: ', input_tensor)
print('Is input tensor infinite? ', input_tensor.isinf())