'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nan_to_num\ntorch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)\n'
import torch
_input_tensor = torch.tensor([[1, 0, (- 1)], [2, (- 2), (- 2)], [3, (- 3), (- 3)]], dtype=torch.float)
_output_tensor = torch.Tensor.nan_to_num(_input_tensor, nan=0.0, posinf=None, neginf=None)
print(_output_tensor)