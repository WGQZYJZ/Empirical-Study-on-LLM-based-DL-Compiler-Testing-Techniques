'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
x = torch.randn(2, 3, requires_grad=True)
torch.nn.init.normal_(x)
print(x)
'\nOutput:\ntensor([[-0.5587, -0.1407, -0.8481],\n        [-0.5456, -0.5209, -0.4240]], requires_grad=True)\n'