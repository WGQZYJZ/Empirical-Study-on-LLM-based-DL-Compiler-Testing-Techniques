input = torch.tensor([1, 2, 3, 4, 4, 3, 2, 1])
input = input.unsqueeze(0).unsqueeze(0)
output = torch.unique_consecutive(input, return_inverse=True, return_counts=True, dim=None)