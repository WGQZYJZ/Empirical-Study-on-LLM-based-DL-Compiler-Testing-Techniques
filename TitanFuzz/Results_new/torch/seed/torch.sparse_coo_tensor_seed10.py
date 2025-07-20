indices = np.array([[0, 1, 1], [2, 0, 2]])
values = np.array([1, 2, 3])
torch_sparse_tensor = torch.sparse_coo_tensor(indices, values)