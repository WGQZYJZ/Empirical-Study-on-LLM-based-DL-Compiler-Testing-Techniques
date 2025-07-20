input_tensor = torch.tensor([[1, (- 1), (- 1), 1, 1], [1, (- 1), 1, (- 1), (- 1)]], dtype=torch.float32)
torch.Tensor.sgn_(input_tensor)