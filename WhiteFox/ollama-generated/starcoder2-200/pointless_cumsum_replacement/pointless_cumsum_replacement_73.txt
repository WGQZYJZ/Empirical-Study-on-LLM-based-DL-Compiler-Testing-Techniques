
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg0, arg1):
        v2 = torch.full([arg0[arg1], 8597], 1, dtype=dtype, layout=layout, device=device)
        v3 = convert_element_type(v2, dtype)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
arg0 = torch.randn(58647).to(device)
__arg1  = [int(x) for x in np.random.choice(2, arg0[0].shape)] # Index for dimension 0 of argument 1
