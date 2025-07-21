'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_per_channel_axis\ntorch.Tensor.q_per_channel_axis(_input_tensor)\n'
import torch
_input_tensor = torch.randint(0, 255, (1, 3, 32, 32), dtype=torch.uint8)
torch.Tensor.q_per_channel_axis(_input_tensor)