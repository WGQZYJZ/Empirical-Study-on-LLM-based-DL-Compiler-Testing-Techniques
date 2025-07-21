'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
x = torch.randn(3, 3)
model = torch.nn.Sequential(torch.nn.Linear(3, 2), torch.nn.ReLU(), torch.nn.Linear(2, 1), torch.nn.ReLU())
print(model)