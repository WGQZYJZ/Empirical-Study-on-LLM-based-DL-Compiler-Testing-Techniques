input_tensor = torch.rand(3, 5)
indices = torch.tensor([[0, 1], [2, 3]])
values = torch.tensor([[0.1, 0.2], [0.3, 0.4]])
output = torch.Tensor.index_put_(input_tensor, indices, values)