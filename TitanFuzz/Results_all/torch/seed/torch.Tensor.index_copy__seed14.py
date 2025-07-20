_input_tensor = torch.randn(4, 3)
torch.Tensor.index_copy_(_input_tensor, dim=0, index=torch.tensor([2, 3, 0, 1]), tensor=torch.tensor([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]))