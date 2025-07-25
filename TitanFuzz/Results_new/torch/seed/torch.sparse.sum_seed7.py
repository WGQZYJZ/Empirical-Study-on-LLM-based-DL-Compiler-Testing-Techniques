indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
sparse_tensor = torch.sparse_coo_tensor(indices, values, torch.Size([3, 3]))
sum_result = torch.sparse.sum(sparse_tensor, dim=0)
sum_result = torch.sparse.sum(sparse_tensor, dim=1)