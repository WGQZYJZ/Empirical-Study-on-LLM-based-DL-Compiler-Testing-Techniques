input_tensor = torch.randn(3, 3)
unbind_tensor = torch.unbind(input_tensor, dim=0)
for i in unbind_tensor:
    print(i)