input_tensor = torch.rand(5, 3)
index_tensor = torch.LongTensor([0, 2])
copy_tensor = torch.rand(2, 3)
output_tensor = torch.Tensor.index_copy(input_tensor, 0, index_tensor, copy_tensor)