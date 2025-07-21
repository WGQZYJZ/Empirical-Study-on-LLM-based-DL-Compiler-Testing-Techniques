'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_output_tensor = _input_tensor.values()
print(_output_tensor)