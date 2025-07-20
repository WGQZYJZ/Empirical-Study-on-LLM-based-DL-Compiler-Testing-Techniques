input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.index_fill(input_tensor, 1, torch.tensor([0, 2]), 0)