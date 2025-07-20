input = torch.sparse_coo_tensor(torch.tensor([[0, 1, 1], [2, 0, 2]]), torch.tensor([1, 2, 3]), torch.Size([3, 3]))
output = torch.sparse.sum(input, dim=0)