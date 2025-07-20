input = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.argmax(input, dim=0)
torch.argmax(input, dim=1, keepdim=True)
torch.argmax(input, dim=1, keepdim=False)