'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
input_tensor = torch.randn(1, 3, 5)
diff_tensor = input_tensor.diff(n=1, dim=(- 1), prepend=None, append=None)
print(diff_tensor)