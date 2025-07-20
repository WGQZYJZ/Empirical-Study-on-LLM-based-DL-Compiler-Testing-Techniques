input_tensor = torch.randn(3, 3)
torch.Tensor.index_copy_(input_tensor, 0, torch.LongTensor([0, 2]), torch.randn(2, 3))