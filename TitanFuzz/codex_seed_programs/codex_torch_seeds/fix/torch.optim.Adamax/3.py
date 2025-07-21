'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
input_data = torch.randn(3, requires_grad=True)
print(input_data)
optimizer = torch.optim.Adamax([input_data], lr=0.01)
optimizer.zero_grad()
input_data.retain_grad()
loss = input_data.sum()
loss.backward()
optimizer.step()
print(input_data)
print(input_data.grad)