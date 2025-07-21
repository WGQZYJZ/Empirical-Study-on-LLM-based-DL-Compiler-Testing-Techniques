'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square_\ntorch.Tensor.square_(_input_tensor)\n'
import torch
input_data = torch.arange((- 2), 3)
print('input_data: ', input_data)
torch.Tensor.square_(input_data)
print('square_input_data: ', input_data)