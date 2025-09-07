
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       v1 = torch.cat([x1, x2], dim=0) 
       v2 = v1.view(-1, 3 * 4) 
       return torch.relu(v2)


# Initializing the model
m = Model()

# Inputs to the model (first input to the model is always `x`)
x1 = torch.randn(65537,) # x1
x2 = torch.randn(65538, 40) # x2 

