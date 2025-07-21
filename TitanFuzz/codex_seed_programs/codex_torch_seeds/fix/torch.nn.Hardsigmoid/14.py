'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardsigmoid\ntorch.nn.Hardsigmoid(inplace=False)\n'
import torch
import numpy as np
print(torch.__version__)
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
print(input_data)
hardsigmoid = torch.nn.Hardsigmoid()
output = hardsigmoid(input_data)
print(output)