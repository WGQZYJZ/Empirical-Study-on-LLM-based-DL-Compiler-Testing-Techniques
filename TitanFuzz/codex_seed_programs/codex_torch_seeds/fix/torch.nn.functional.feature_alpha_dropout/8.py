'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import numpy as np
input = torch.randn(10, 3)
print(input)
output = torch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
print(output)