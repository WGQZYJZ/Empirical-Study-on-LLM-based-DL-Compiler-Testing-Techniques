
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1, x2], 1, dtype=torch.float32, layout=torch.strided, device="cuda:0", pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1).to("cuda:0")
x2 = torch.randn(2).to("cuda:0")
