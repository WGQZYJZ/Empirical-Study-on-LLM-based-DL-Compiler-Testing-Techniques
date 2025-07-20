input_data = torch.randn(3, 5)
output = torch.norm(input_data, p=2, dim=1, keepdim=False, out=None, dtype=None)
output = torch.norm(input_data, p=2, dim=0, keepdim=False, out=None, dtype=None)
output = torch.norm(input_data, p=2, dim=None, keepdim=False, out=None, dtype=None)