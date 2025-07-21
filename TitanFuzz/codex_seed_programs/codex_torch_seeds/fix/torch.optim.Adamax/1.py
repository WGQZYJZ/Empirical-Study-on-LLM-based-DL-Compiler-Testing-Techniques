'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
print('Input data: ', input_data)
optimizer = torch.optim.Adamax([input_data], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
print('Default values: ', optimizer.defaults)
optimizer.step()
print('Data After 1st iteration: ', input_data)
optimizer.step()
print('Data After 2nd iteration: ', input_data)