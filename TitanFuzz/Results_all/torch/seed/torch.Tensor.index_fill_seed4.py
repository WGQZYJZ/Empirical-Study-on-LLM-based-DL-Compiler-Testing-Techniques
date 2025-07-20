input_tensor = torch.tensor([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
output_tensor = torch.Tensor.index_fill(input_tensor, 0, torch.tensor([0, 2]), 1)