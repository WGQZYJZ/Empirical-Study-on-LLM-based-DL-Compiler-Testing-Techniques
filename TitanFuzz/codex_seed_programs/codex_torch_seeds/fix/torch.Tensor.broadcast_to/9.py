'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.broadcast_to\ntorch.Tensor.broadcast_to(_input_tensor, shape)\n'
import torch
input_data = torch.arange(1, 5, dtype=torch.float32).reshape(1, 2, 2)
output_data = torch.Tensor.broadcast_to(input_data, (2, 2, 2))
print(output_data)