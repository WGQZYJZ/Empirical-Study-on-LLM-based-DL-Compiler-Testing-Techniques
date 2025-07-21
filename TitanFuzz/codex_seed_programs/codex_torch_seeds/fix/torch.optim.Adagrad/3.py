'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adagrad\ntorch.optim.Adagrad(params, lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0, eps=1e-10)\n'
import torch
import torch.nn as nn
import torch
x = torch.tensor([3.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
adagrad = torch.optim.Adagrad([x, y], lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0, eps=1e-10)
loss_fn = torch.nn.MSELoss(reduction='sum')
for epoch in range(10):
    pred = (x * y)
    loss = loss_fn(pred, torch.tensor([10.0]))
    print('Epoch: ', epoch, 'Loss: ', loss.item())