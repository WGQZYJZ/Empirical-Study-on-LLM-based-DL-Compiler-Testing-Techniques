
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer  = nn.Linear(1024, 1)
 
    def forward(self, x1):
        return self.layer(x1) * inv_scale
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
