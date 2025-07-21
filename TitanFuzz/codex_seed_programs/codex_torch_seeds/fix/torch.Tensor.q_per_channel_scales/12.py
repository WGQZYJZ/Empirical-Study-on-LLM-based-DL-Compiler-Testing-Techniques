'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_scales\ntorch.Tensor.q_per_channel_scales(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = input_tensor.q_per_channel_scales()
print('The output tensor is: ', output_tensor)