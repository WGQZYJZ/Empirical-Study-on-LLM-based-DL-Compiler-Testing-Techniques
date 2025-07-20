x = torch.Tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
y = torch.Tensor([[1], [2], [3], [4]])
dataset = torch.utils.data.TensorDataset(x, y)
for i in range(len(dataset)):
    print(dataset[i])