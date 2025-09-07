
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256*14, 10)
        self.relu  = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = self.relu(v2)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(64, 256*14)
other_tensor  = torch.randn(64, 10)
__output__  = m(x1)


