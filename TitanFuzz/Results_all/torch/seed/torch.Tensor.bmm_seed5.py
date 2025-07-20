input_tensor = torch.randint(low=0, high=10, size=(3, 2, 4), dtype=torch.float32)
batch2 = torch.randint(low=0, high=10, size=(3, 4, 5), dtype=torch.float32)
output_tensor = torch.Tensor.bmm(input_tensor, batch2)