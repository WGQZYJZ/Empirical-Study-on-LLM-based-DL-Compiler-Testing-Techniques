'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adam\ntorch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)\n'
import torch
params = torch.tensor([1.0, 0.0], requires_grad=True)
print(params)
learning_rate = 0.001
optimizer = torch.optim.Adam([params], lr=learning_rate)
print(optimizer)
for _ in range(20):
    optimizer.zero_grad()
    loss = (((params[0] - 3) ** 2) + ((params[1] - 2) ** 2))
    loss.backward()
    optimizer.step()
    print(params)
print(f'params = {params}')