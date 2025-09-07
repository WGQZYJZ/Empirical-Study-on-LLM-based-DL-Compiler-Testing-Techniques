
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 512)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x):
        v3 = torch.sigmoid(v1)
        v4 = v2 * v3
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 512)