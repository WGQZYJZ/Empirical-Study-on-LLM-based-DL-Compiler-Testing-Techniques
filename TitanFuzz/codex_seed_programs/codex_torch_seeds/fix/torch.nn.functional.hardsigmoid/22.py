'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
if True:
    input = torch.randn(1, 3)
    output = torch.nn.functional.hardsigmoid(input)
    print(output)