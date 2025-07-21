'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square\ntorch.Tensor.square(_input_tensor)\n'
import torch
_input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
_output_data = torch.Tensor.square(_input_data)
print(_output_data)