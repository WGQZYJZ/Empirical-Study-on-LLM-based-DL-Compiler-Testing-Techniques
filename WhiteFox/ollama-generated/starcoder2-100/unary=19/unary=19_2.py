
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48*64*32, 1)
 
    def forward(self, x1):
        v0 = torch.flatten(x1, start_dim=1, end_dim=-1).type(torch.float32)
        v1 = self.linear(v0)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(5, 48, 64, 32)
__output__  = m(x1)

