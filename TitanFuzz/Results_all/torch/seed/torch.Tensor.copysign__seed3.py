input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
torch.Tensor.copysign_(input_tensor, other)