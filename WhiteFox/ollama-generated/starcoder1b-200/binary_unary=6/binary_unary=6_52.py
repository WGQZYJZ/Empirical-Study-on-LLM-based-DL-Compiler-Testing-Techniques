
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2, bias=True)
 
    def forward(self, x1, other=0):
        v1 = self.linear(x1) - other
        v2 = F.relu(v1)
        return v2


# Initializing the model
m = Model()

