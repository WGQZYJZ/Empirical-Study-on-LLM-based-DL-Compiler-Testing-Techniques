input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.gather(input_tensor, 1, torch.tensor([[1, 0, 2], [0, 1, 2]]))