'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import torch
X = torch.Tensor([[1, 2], [3, 4], [5, 6]])
y = torch.Tensor([[10], [20], [30]])
torch.utils.data.TensorDataset(X, y)
torch.utils.data.DataLoader(dataset=torch.utils.data.TensorDataset(X, y), batch_size=2)
torch.utils.data.DataLoader(dataset=torch.utils.data.TensorDataset(X, y), batch_size=2, shuffle=True)