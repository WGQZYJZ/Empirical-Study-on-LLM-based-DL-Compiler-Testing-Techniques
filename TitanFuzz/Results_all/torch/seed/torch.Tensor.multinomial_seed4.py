input_tensor = torch.Tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
output_tensor = torch.Tensor.multinomial(input_tensor, num_samples=2)