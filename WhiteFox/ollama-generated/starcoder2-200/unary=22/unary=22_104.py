t0  = 1 - x1  # Apply the function `torch.pow(1, x)` to each element in a tensor `x`
t3  = t0 * t2 + torch.erf(t4) * torch.tan(t5) + 1 / (1 + torch.sinh(torch.tensor([0, 360], dtype=float32)))  # Apply the function `torch.sqrt(x)` to each element in a tensor `x`
