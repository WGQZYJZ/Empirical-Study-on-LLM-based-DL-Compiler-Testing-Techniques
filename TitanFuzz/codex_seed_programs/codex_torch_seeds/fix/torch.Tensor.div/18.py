'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div\ntorch.Tensor.div(_input_tensor, value, *, rounding_mode=None)\n'
import torch
data = [1, 2, 3, 4, 5]
tensor = torch.tensor(data)
print('tensor:', tensor)
tensor_div = tensor.div(2)
print('tensor_div:', tensor_div)