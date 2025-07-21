'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atan2\ntorch.Tensor.atan2(_input_tensor, other)\n'
import torch
input_tensor = torch.arange((- 5), 6)
other_tensor = torch.arange(1, 12)
atan2_tensor = input_tensor.atan2(other_tensor)
print('input_tensor:', input_tensor)
print('other_tensor:', other_tensor)
print('atan2_tensor:', atan2_tensor)