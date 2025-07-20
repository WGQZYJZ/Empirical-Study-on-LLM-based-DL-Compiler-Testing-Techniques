input_tensor = torch.rand(3, 3)
new_tensor = torch.Tensor.copy_(input_tensor)
new_tensor = torch.Tensor.copy_(input_tensor, dtype=torch.int32)