
model = torch.nn.Sequential(torch.nn.Linear(200, 1))
input_tensor = torch.randn(32, 200).to('cuda')
output_tensor = model(input_tensor)

