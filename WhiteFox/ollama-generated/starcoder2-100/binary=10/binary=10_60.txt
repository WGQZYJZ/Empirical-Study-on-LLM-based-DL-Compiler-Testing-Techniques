
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 384)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        return v2


# Initializing the model with a different input tensor for testing
other = torch.zeros_like(x1[0])
m  = Model()
__output__  = m(x1)
 
