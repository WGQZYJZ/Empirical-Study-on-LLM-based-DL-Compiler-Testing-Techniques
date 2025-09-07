
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v4 = -0.75 # Replace this with the negative slope of LeakyReLU 
        v3 = v1 * v4
        v6 = torch.where(v2, v1, v3)
        return v6


# Initializing the model