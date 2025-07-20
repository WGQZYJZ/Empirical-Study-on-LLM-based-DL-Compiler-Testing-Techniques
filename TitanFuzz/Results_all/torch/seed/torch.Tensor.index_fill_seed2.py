input_tensor = torch.randn(3, 3)
result = torch.Tensor.index_fill(input_tensor, 1, torch.LongTensor([0, 2]), 0)