'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt_\ntorch.Tensor.sqrt_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
torch.Tensor.sqrt_(input_tensor)
print('input_tensor: ', input_tensor)
print('input_tensor.sqrt_(): ', input_tensor.sqrt_())