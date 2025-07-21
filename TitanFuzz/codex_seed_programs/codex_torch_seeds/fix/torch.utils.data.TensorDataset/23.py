'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import torch
x = torch.tensor(3.0)
y = torch.tensor(4.0)
z = (x * y)
print(z)
x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
y = torch.tensor([2, 2, 2, 2, 2], dtype=torch.float32)
dataset = torch.utils.data.TensorDataset(x, y)
print(dataset)
data_loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=2, shuffle=True)
for (x_batch, y_batch) in data_loader:
    print(x_batch, y_batch)