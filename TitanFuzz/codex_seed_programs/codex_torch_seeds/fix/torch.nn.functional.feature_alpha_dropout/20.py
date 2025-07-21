'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
import torch.nn.functional as F
x = torch.randn(1, 1, 3, 3, requires_grad=True)
y = F.feature_alpha_dropout(x, p=0.5, training=False, inplace=False)
print(x)
print(y)