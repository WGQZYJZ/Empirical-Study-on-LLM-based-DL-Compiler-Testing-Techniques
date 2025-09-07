
model = torch.nn.Linear(2, 2)

# Inputs to the model
input1 = torch.randn(2) # random tensor of size (2,)
input2 = torch.tensor([0., 50., -49., 37]) # 4 element 1D tensor

# Expected results
res_1 = model(input1, 1)
res_2 = model(input2[None, :], None)

