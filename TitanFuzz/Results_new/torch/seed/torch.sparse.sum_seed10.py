indices = torch.tensor([[0, 1], [1, 0]])
values = torch.tensor([1, 1], dtype=torch.float32)
sparse_mx = torch.sparse_coo_tensor(indices, values, [2, 2])
sum_sparse_mx = torch.sparse.sum(sparse_mx, dim=0)