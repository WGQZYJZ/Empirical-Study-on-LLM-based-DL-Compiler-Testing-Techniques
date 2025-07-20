input_tensor = torch.randint(1, 10, (3, 3))
output_tensor = torch.Tensor.lcm(input_tensor, torch.tensor([1, 2, 3]))
output_tensor = torch.lcm(input_tensor, torch.tensor([1, 2, 3]))