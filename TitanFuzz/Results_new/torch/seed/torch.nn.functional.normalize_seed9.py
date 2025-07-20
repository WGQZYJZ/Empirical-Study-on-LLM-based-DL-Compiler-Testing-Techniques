data = np.array([[3, 4], [5, 6]])
data = torch.tensor(data, dtype=torch.float)
torch.nn.functional.normalize(data, p=2.0, dim=1, eps=1e-12, out=None)
torch.nn.functional.normalize(data, p=1.0, dim=1, eps=1e-12, out=None)