import torch

x = torch.tensor(3.0)
y = torch.tensor(4.0)
z = (x * y)
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
y = torch.tensor([2, 2, 2, 2, 2], dtype=torch.float32)
dataset = torch.utils.data.TensorDataset(x, y)
data_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=2, shuffle=True)
for (x_batch, y_batch) in data_loader:
    print(x_batch, y_batch)