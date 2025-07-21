import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(10, 3)
target_data = torch.randint(0, 3, (10,), dtype=torch.int64)
loss_fn = torch.nn.CrossEntropyLoss()
model = torch.nn.Linear(3, 3)
optimizer = torch.optim.SGD(model.parameters(), lr=0.05)
for epoch in range(100):
    optimizer.zero_grad()
    output = model(input_data)
    loss = loss_fn(output, target_data)
    loss.backward()
    optimizer.step()
    torch.nn.utils.clip_grad_value_(model.parameters(), 0.1)
    print(f'Epoch {epoch}, Loss {loss.item()}')