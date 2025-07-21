'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adam\ntorch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)\n'
import torch
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
optimizer = torch.optim.Adam([input_data], lr=0.1)
print(input_data.data)
optimizer.zero_grad()
output = (input_data * input_data)
loss = output.mean()
loss.backward()
optimizer.step()
print(input_data.data)