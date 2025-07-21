'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder\ntorch.Tensor.remainder(_input_tensor, divisor)\n'
import torch
_input_tensor = torch.tensor([10, 20, 30, 40], dtype=torch.float32)
_result_tensor = _input_tensor.remainder(divisor=3)
print(_result_tensor)