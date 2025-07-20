input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([11, 12])
output_tensor = torch.Tensor.index_put_(input_tensor, indices, values, accumulate=False)