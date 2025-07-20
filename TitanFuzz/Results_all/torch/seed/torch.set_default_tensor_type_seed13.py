data = np.array([1, 2, 3, 4, 5, 6])
data = data.astype(np.float32)
x = torch.from_numpy(data)
torch.set_default_tensor_type(torch.FloatTensor)