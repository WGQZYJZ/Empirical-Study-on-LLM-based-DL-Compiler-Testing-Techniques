input_tensor = torch.rand(4, 4)
output_tensor = torch.Tensor.clip_(input_tensor, min=0.3, max=0.6)