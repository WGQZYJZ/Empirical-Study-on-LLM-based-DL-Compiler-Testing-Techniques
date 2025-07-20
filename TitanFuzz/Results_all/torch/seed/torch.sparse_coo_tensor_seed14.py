indices = torch.tensor([[0, 1], [1, 0]])
values = torch.tensor([1, 1])
size = torch.Size([2, 2])
output = torch.sparse_coo_tensor(indices, values, size)