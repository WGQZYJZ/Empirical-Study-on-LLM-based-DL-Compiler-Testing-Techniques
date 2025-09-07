
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.linear = torch.nn.Linear(d_model, 8, bias=False)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ... ,v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 512)
x2 = torch.randn(8, 512)
