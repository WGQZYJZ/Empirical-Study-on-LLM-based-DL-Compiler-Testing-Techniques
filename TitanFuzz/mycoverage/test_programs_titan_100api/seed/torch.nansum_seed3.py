input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], dtype=torch.float32)
torch.nansum(input, dim=1, keepdim=True)
torch.nansum(input, dim=1, keepdim=False)
torch.nansum(input, dim=0, keepdim=False)