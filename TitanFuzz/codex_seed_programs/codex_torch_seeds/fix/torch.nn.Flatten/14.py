'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4, 5)
flatten_layer = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
flatten_tensor = flatten_layer(input_tensor)
print('Input tensor: ', input_tensor.shape)
print('Flatten tensor: ', flatten_tensor.shape)