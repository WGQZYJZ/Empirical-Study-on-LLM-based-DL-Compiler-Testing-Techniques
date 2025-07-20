_input_tensor = torch.randn(3, 5)
dim = 1
index = torch.LongTensor([0, 2, 4])
tensor2 = torch.randn(3, 3)
torch.Tensor.index_copy(_input_tensor, dim, index, tensor2)