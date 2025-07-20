input_tensor = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
torch.Tensor.allclose(input_tensor, other)