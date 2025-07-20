input_tensor = torch.rand(1, 1, 1, 1)
is_inference = torch.Tensor.is_inference(input_tensor)