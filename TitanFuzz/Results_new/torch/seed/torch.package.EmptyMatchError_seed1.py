input_data = torch.randn(1, 1, 32, 32)
try:
    torch.package.EmptyMatchError()
except Exception as e:
    print(e)