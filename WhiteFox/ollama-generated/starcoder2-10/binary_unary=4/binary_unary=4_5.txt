
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 32 * 16, 50)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + kwargs["other"]
        v3  = torch.relu(v2) 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
other  = torch.randn(50,)
x1     = torch.randn(1, 32 * 32 * 16)
__output__  = m(x1, other=other)


