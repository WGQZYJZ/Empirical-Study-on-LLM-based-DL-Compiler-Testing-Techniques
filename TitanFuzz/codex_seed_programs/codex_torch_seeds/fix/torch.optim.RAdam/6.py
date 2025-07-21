'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
from torch.utils.data import Dataset, DataLoader
import torch
input_data = torch.randn(100, 3)
output_data = torch.randn(100, 2)
from torch.optim import RAdam
model = torch.nn.Linear(3, 2)
optimizer = RAdam(model.parameters(), lr=0.001)
for i in range(100):
    optimizer.zero_grad()
    output = model(input_data)
    loss = torch.nn.functional.mse_loss(output, output_data)
    loss.backward()
    optimizer.step()
print(model.weight)
print(model.bias)