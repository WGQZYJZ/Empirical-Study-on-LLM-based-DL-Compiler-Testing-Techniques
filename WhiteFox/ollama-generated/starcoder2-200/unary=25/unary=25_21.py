
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2)
        v2  = (v1 > 0).float() * -1 +  (v1 <= 0).float()
        v3  = v1 * v2 # Negative slope is set to `-1`
        v4  = torch.where(v2, x1, v3) 
        return v4

# Initializing the model
m  = Model()

# Inputs for the model
x1 = torch.randn(100).view(-1, 50)

