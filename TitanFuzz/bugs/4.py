import torch

x = torch.ones(2)
y = torch.sin(x)
y = torch.arcsin(y)  # inverse operations, gives [1.0000, 1.0000]
y = torch.arccos(y)
print(y) # gives [0.0003, 0.0003]

x1 = x.clone().cuda()
y1 = torch.sin(x1)
y1 = torch.arcsin(y1) # gives [1.0000, 1.0000]
y1 = torch.arccos(y1)
print(y1) # gives [nan, nan]