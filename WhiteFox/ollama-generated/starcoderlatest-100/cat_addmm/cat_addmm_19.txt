
class Model(torch.nn.Module):
    def __init__(self, d_in=48, d_out=1024, dim=1):
        super().__init__()
        self.fc = torch.nn.Linear(d_in, d_out)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1 * 0.5
        v3 = v1 + v2
        v4 = torch.cat([v3], dim)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
