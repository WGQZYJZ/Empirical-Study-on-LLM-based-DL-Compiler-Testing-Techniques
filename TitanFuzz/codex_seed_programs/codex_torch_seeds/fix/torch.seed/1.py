'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
import numpy as np
'\nTask 1: Generate input data\n'
input_data = np.random.rand(2, 3)
print(input_data)
'\nTask 2: Call the API torch.seed\ntorch.seed()\n'
torch.seed()
'\nTask 3: Call the API torch.rand\ntorch.rand()\n'
print(torch.rand(2, 3))
'\nTask 4: Call the API torch.randn\ntorch.randn()\n'
print(torch.randn(2, 3))
'\nTask 5: Call the API torch.randint\ntorch.randint()\n'
print(torch.randint(2, 3, (2, 3)))
'\nTask 6: Call the API torch.randperm\ntorch.randperm()\n'
print(torch.randperm(3))
'\nTask 7: Call the API torch.rand_like\ntorch.rand_like()\n'
input_data = torch.rand(2, 3)