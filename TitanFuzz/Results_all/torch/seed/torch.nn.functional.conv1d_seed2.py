input = torch.tensor(np.array([1, 2, 3, 4]).reshape(1, 1, 4), dtype=torch.float32)
weight = torch.tensor(np.array([1, 2, 3]).reshape(1, 1, 3), dtype=torch.float32)
output = torch.nn.functional.conv1d(input, weight)