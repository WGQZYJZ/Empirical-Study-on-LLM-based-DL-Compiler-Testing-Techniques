input = torch.randn(5, 5)
torch.amax(input)
torch.amax(input, dim=0)
torch.amax(input, dim=0, keepdim=True)
torch.amax(input, dim=(- 1))
torch.amax(input, dim=(- 1), keepdim=True)