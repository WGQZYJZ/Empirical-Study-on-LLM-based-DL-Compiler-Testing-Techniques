input = torch.sparse_coo_tensor(torch.tensor([[0, 1, 1], [2, 0, 2]]), torch.tensor([3, 4, 5]), torch.Size([3, 3]))
result = torch.sparse.sum(input, dim=None, dtype=None)