
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256, 4096)
        self.relu1 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 - other_value
        v3  = self.relu1(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(64, 256)
