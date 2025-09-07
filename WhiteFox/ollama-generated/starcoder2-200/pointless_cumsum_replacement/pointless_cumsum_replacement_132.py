
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = torch.full([75386429342, 7538], dtype=torch.float16) 
        v1  = convert_element_type(v0, torch.float16)  
        v2  = torch.cumsum(v1, 1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(75386429342, 7538)
