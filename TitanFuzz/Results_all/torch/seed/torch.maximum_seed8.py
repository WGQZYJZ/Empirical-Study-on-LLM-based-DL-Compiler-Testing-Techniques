input = torch.rand(2, 3)
other = torch.rand(2, 3)
torch.maximum(input, other)
input = torch.rand(2, 3)
other = torch.rand(2, 3)
torch.max(input)
torch.max(input, dim=0, keepdim=False)
torch.max(input, other)