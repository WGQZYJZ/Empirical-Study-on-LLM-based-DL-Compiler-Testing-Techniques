_input_tensor = torch.randn(4, 4, dtype=torch.float32)
other = torch.randn(4, 4, dtype=torch.float32)
torch.Tensor.igammac_(_input_tensor, other)