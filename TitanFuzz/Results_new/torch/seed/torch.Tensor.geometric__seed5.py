input_tensor = torch.rand(3, 3)
p = 0.5
output_tensor = torch.Tensor.geometric_(input_tensor, p)