input_tensor = torch.randint(low=0, high=10, size=(3, 3))
other = torch.randint(low=0, high=10, size=(3, 3))
torch.Tensor.ge_(input_tensor, other)