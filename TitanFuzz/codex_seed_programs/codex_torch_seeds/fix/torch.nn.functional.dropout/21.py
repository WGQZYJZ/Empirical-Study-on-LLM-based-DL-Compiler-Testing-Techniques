'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
x = torch.randn(100, 100)
y = torch.nn.functional.dropout(x, p=0.5, training=True)
print(x)
print(y)
'\nTask 4: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
dropout = torch.nn.Dropout(p=0.5)
y = dropout(x)
print(x)
print(y)
'\nTask 5: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
dropout = torch.nn.Dropout2d(p=0.5)
y = dropout(x.view(100, 1, 100, 1))
print(x)
print(y)