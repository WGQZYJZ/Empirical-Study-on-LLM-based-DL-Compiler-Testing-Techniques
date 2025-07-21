'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.negative\ntorch.Tensor.negative(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_output_tensor = _input_tensor.negative()
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)