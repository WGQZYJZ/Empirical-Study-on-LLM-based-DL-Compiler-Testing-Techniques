'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tolist\ntorch.Tensor.tolist(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 224, 224)
_output_tensor = torch.Tensor.tolist(_input_tensor)
print(_output_tensor)