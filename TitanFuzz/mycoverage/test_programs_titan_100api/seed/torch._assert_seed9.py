input = torch.randn(3, 3)
torch._assert(input.is_floating_point(), 'input must be floating point')