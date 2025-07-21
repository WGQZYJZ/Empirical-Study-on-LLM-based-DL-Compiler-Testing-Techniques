'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
input_data = torch.randn(1, 1, requires_grad=True)
target = torch.tensor([[1.0]])
optimizer = optim.RAdam([input_data], lr=0.001)
for i in range(500):
    optimizer.zero_grad()
    output = torch.sigmoid(input_data)
    loss = F.binary_cross_entropy(output, target)
    loss.backward()
    optimizer.step()
    print('Epoch: ', i, 'Loss: ', loss.item())
print('input_data: ', input_data)
print('output: ', output)