input_tensor = torch.randn(1, 1, 3, 3)
squeeze_tensor = torch.Tensor.squeeze(input_tensor, dim=1)