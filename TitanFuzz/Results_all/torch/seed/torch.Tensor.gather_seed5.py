input_tensor = torch.randn(2, 4)
output_tensor = torch.Tensor.gather(input_tensor, dim=1, index=torch.tensor([[0, 1, 2, 3], [1, 2, 3, 0]]))