'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch
x = torch.randn(100, 1000)
y = torch.randn(100, 1000)
linear = torch.nn.Linear(1000, 1000)
dropout = torch.nn.Dropout(p=0.5, inplace=False)
y_pred = dropout(linear(x))
print(y_pred)