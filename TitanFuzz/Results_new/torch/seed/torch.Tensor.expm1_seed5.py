data = np.random.rand(5, 5)
data = torch.tensor(data)
output = torch.Tensor.expm1(data)