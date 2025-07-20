input_tensor = torch.arange(1, 11, dtype=torch.float32)
output_tensor = torch.Tensor.clip_(input_tensor, min=3, max=7)