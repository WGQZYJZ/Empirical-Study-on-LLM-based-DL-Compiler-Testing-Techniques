np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
np_data = torch_data.numpy()
data = [(- 1), (- 2), 1, 2]
tensor = torch.FloatTensor(data)
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor