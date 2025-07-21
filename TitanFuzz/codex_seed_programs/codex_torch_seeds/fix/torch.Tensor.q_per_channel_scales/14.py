'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_scales\ntorch.Tensor.q_per_channel_scales(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=255, size=(1, 3, 224, 224), dtype=torch.uint8)
output_tensor = input_tensor.q_per_channel_scales()
print(output_tensor)