input_tensor = torch.rand(1, 3, 224, 224)
output_tensor = torch.Tensor.q_scale(input_tensor)