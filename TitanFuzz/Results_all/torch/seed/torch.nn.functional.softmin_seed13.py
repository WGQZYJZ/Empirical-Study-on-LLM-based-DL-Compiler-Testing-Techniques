data = np.array([[0.1, 0.2, 0.3, 0.4, 0.5, 0.6]])
data = torch.from_numpy(data)
output = torch.nn.functional.softmin(data, dim=1)