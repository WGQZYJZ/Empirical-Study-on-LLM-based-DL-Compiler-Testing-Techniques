'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print('The input tensor: ', input_tensor)
output_tensor = input_tensor.div_(2)
print('The output tensor: ', output_tensor)