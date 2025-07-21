'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
x = torch.rand(1000, 1000)
y = torch.rand(1000, 1000)
torch.nn.Dropout(p=0.5, inplace=False)
if torch.cuda.is_available():
    device = torch.device('cuda')
    x = x.to(device)
    y = y.to(device)
    z = (x + y)
    print(z)
    print(z.to('cpu', torch.double))