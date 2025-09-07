
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 20)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        return v1 + kwargs["other"]


# Initializing the model
m = Model()
__output__  = m(torch.randn(1, 3), other=torch.zeros((3)))

