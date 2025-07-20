input_tensor = torch.rand(1, 3, 3)
other = torch.rand(1, 3, 3)
torch.Tensor.copysign_(input_tensor, other)