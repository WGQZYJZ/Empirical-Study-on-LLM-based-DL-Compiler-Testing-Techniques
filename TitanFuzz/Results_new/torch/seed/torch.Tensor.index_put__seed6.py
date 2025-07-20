_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = torch.LongTensor([[0, 1], [1, 2]])
values = torch.Tensor([[10, 20], [30, 40]])
torch.Tensor.index_put_(_input_tensor, indices, values, accumulate=True)