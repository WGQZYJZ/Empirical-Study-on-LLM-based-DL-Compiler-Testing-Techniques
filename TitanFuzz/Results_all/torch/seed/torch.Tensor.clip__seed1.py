input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_tensor = torch.Tensor.clip_(input_tensor, min=2.5, max=5.5)