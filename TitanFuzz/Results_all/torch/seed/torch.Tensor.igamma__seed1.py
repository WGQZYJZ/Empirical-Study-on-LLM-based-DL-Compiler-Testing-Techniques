_input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.float32)
other = torch.randint(1, 10, (3, 3), dtype=torch.float32)
torch.Tensor.igamma_(_input_tensor, other)