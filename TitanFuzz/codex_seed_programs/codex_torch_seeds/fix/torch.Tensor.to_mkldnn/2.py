'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3, 4, 5, 6)
_output_tensor = _input_tensor.to_mkldnn()
print(_output_tensor)