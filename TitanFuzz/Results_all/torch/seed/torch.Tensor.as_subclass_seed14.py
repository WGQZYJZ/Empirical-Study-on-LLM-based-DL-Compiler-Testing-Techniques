input_tensor = torch.randn(1, 3, 224, 224, dtype=torch.float32)
torch.Tensor.as_subclass(input_tensor, torch.FloatTensor)