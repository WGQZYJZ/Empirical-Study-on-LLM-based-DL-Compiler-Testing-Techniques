

model = torch.nn.TransformerEncoderLayer(d_model=256, nhead=8)

inputs1 = torch.rand(size=(100, 32))
inputs2 = torch.rand(size=(42,))

inputs = [inputs1] + list(torch.split(inputs2, inputs2[i].numel(), dim=-1)) # Inputs to the model