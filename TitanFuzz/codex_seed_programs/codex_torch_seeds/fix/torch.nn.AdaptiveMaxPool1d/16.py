'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
import torch
input_data = torch.tensor([[[1, 2], [3, 4], [5, 6], [7, 8]]], dtype=torch.float)
pool_output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_data)
print(pool_output)