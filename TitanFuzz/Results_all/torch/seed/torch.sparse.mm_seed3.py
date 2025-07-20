sparse_matrix = torch.sparse_coo_tensor(torch.tensor([[0, 1, 1], [2, 0, 2]]), torch.tensor([3, 4, 5]), torch.Size([3, 3]))
dense_matrix = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = torch.sparse.mm(sparse_matrix, dense_matrix)