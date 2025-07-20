input_tensor = torch.rand(4, 4)
torch.Tensor.clamp_(input_tensor, min=0.0, max=1.0)