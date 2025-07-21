'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
if True:
    input = torch.randn(1, 64, 8, 9, 10)
    output_size = (1, 1, 1)
    print(torch.nn.functional.adaptive_max_pool3d(input, output_size))