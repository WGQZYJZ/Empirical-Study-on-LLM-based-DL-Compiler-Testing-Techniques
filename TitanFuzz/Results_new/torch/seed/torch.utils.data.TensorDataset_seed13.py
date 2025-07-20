x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([[1], [2], [3]])
dataset = torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))