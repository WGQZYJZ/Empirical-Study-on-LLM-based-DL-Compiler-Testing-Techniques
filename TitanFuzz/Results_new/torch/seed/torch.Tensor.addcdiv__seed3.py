input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
tensor2 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
torch.Tensor.addcdiv_(input_tensor, tensor1, tensor2, value=1)