data = torch.randn(100)
torch.clamp(data, min=(- 0.5), max=0.5)
torch.clamp(data, min=(- 0.5), max=0.5, out=data)
data.clamp_((- 0.5), 0.5)