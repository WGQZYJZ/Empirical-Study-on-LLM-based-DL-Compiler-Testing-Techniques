input_tensor = torch.rand(3, 5)
output_tensor = torch.Tensor.index_select(input_tensor, 0, torch.LongTensor([0, 2]))