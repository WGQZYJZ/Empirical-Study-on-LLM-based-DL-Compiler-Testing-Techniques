_input_tensor = torch.randn(2, 3)
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.randn(2, 2)
torch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)