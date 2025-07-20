indices = torch.LongTensor([[0, 1, 1], [2, 0, 2]])
values = torch.FloatTensor([3, 4, 5])
sparse_tensor = torch.sparse_coo_tensor(indices, values)