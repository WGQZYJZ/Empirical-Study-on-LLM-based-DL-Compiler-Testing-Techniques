'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unbind\ntorch.unbind(input, dim=0)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
unbind_tensor = torch.unbind(input_tensor, dim=0)
print(unbind_tensor)
for i in unbind_tensor:
    print(i)