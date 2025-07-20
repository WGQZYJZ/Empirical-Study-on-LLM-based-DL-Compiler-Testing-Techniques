x = torch.tensor([[1, (- 1)], [1, (- 1)]], dtype=torch.float32)
silu_out = torch.nn.functional.silu(x)