'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_scales\ntorch.Tensor.q_per_channel_scales(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(3, 4, 5, 6, dtype=torch.float)
output_tensor = input_tensor.q_per_channel_scales()
print(output_tensor)