'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
other_tensor = torch.rand(3, 3)
sub_tensor = input_tensor.sub(other_tensor)
print(sub_tensor)