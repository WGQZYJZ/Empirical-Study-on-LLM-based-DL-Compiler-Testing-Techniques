indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
values = torch.tensor([3, 4, 5], dtype=torch.float32)
result = torch.sparse_coo_tensor(indices, values)
result = torch.sparse_coo_tensor(indices, values, size=[3, 3])