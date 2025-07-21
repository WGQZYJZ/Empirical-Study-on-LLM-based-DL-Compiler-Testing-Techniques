'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn\ntorch.randn(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.randn(10, 3)
output_data = torch.randn(10, 2)
loss_fn = torch.nn.MSELoss(reduction='sum')
model = torch.nn.Linear(3, 2)
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
for t in range(500):
    y_pred = model(input_data)
    loss = loss_fn(y_pred, output_data)
    print(t, loss.item())
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()