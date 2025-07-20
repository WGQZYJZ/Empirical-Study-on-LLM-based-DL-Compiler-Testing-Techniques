input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.index_copy_(input_tensor, 0, torch.LongTensor([0, 2]), torch.Tensor([[11, 12, 13], [14, 15, 16]]))