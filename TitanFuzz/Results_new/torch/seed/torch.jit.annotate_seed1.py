x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
x_jit = torch.jit.annotate(torch.Tensor, x)