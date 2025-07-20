_input_tensor = torch.rand(4, 4)
indices = torch.LongTensor([[0, 0], [1, 1], [2, 2], [3, 3]])
values = torch.Tensor([1, 1, 1, 1])
torch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)