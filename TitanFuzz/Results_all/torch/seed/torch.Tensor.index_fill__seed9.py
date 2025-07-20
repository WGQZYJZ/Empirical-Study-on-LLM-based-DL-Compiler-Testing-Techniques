input_tensor = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
torch.Tensor.index_fill_(input_tensor, 0, torch.tensor([1]), torch.tensor(0))