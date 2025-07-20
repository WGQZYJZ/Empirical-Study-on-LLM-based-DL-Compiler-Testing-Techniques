start = torch.tensor([1.0, 1.0, 1.0], dtype=torch.float32)
end = torch.tensor([2.0, 2.0, 2.0], dtype=torch.float32)
torch.Tensor.lerp_(start, end, weight=0.5)