input_tensor = torch.rand(4, 4)
other_tensor = torch.rand(4, 4)
torch.Tensor.isclose(input_tensor, other_tensor, rtol=1e-05, atol=1e-08, equal_nan=False)