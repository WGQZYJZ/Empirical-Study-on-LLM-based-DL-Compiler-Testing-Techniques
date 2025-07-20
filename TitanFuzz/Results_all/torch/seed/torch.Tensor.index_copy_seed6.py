input_tensor = torch.randn(2, 3)
index = torch.LongTensor([1, 0, 2, 1])
tensor2 = torch.randn(4, 3)
output_tensor = torch.Tensor.index_copy(input_tensor, dim=0, index=index, tensor2=tensor2)