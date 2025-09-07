
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8*8*3, 16)
 
    def forward(self, x1):
        v0 = torch.nn.Flatten()(x1)
        v1  = self.linear(v0)
        return relu(v1)

# Initializing the model
m = Model()

