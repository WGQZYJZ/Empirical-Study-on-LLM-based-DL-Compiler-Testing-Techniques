'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
weight = torch.tensor([[0.1, 0.2], [0.3, 0.4]], requires_grad=True)
weight_sparse = torch.tensor([[0.1, 0.0], [0.0, 0.4]], requires_grad=True)
optimizer = torch.optim.SparseAdam([weight_sparse], lr=0.001)
optimizer.zero_grad()
loss = weight.pow(2).sum()
loss.backward()
optimizer.step()
print(weight_sparse.data)