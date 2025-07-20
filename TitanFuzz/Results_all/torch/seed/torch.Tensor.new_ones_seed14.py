input_tensor = torch.rand(1, 2, 3, 4)
output_tensor = torch.Tensor.new_ones(input_tensor, (1, 2, 3, 4), dtype=torch.float32, device=torch.device('cpu'), requires_grad=True)