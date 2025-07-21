'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Rprop\ntorch.optim.Rprop(params, lr=0.01, etas=(0.5, 1.2), step_sizes=(1e-06, 50))\n'
import torch
data = torch.rand(10, requires_grad=True)
print(data)
optimizer = torch.optim.Rprop(params=[data], lr=0.01, etas=(0.5, 1.2), step_sizes=(1e-06, 50))
for i in range(10):
    optimizer.zero_grad()
    output = data.sigmoid()
    loss = output.sum()
    loss.backward()
    optimizer.step()
    print(loss)
    print(data)
    print(data.grad)