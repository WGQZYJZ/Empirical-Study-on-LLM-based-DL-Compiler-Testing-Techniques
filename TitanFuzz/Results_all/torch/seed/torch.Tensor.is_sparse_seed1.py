_input_tensor = torch.sparse_coo_tensor(torch.tensor([[0, 1, 1], [2, 0, 2]]), torch.tensor([0, 1, 2]), torch.Size([3, 3]))
torch.Tensor.is_sparse(_input_tensor)