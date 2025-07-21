'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(1, 3)
linear_model = nn.Linear(3, 1)
print('W: ', linear_model.weight)
print('b: ', linear_model.bias)
y_pred = linear_model(input_data)
print('The prediction: ', y_pred)
criterion = nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(linear_model.parameters(), lr=0.01)
y_pred = linear_model(input_data)
loss = criterion(y_pred, torch.tensor([[0.0]]))
print('The loss: ', loss.item())
loss.backward()