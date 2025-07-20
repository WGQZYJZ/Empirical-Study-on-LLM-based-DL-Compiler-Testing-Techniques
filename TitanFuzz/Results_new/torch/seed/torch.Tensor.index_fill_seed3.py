input_tensor = torch.rand(3, 5)
output_tensor = torch.Tensor.index_fill(input_tensor, 0, torch.tensor([1, 2]), 1)