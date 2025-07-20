input_tensor = torch.rand(3, 4)
index = torch.LongTensor([[0, 1], [2, 0]])
src = torch.rand(2, 2)
output_tensor = torch.Tensor.scatter_add(input_tensor, 0, index, src)