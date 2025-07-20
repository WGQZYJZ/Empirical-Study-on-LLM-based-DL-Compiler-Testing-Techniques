tensor_1 = torch.tensor([[1, 2], [3, 4]])
tensor_2 = torch.tensor([[5, 6], [7, 8]])
tensor_3 = torch.tensor([[9, 10], [11, 12]])
torch.block_diag(tensor_1, tensor_2, tensor_3)