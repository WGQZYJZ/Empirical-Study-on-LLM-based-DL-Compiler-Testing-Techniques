x = np.array([[1, 2], [3, 4]])
y = torch.from_numpy(x)
torch.set_default_tensor_type(torch.FloatTensor)
z = torch.from_numpy(x)