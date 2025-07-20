input_tensor = torch.randn(2, 3)
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([1.0, 2.0])
torch.Tensor.index_put_(input_tensor, indices, values, accumulate=False)