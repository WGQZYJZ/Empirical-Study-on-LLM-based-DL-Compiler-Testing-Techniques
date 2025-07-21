'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
import torch
x_data = torch.tensor([[1.0], [2.0], [3.0]], dtype=torch.float32)
y_data = torch.tensor([[2.0], [4.0], [6.0]], dtype=torch.float32)
w = torch.tensor([[0.0]], dtype=torch.float32, requires_grad=True)
optimizer = torch.optim.SparseAdam([w], lr=0.1)
y_pred = x_data.mm(w)
loss = (y_pred - y_data).pow(2).sum()
print('loss: ', loss.item())