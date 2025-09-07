
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.split(x1, 4803) 
        v7  = [v2[i] for i in range(len([4803]))]
        v9  = torch.cat(v7, dim=0)
        return v9


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(256*2, 192, 4803) 
 