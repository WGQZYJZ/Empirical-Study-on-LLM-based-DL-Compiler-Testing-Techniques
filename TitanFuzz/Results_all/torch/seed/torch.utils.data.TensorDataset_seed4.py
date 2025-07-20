x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[10], [20]])
dataset = torch.utils.data.TensorDataset(x, y)