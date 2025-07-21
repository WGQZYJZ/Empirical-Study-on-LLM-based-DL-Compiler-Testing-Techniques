'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isfinite\ntorch.Tensor.isfinite(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.isfinite(_input_tensor)
print(_output_tensor)
'\nOutput:\ntensor([[1, 1, 1],\n        [1, 1, 1],\n        [1, 1, 1]], dtype=torch.uint8)\n'