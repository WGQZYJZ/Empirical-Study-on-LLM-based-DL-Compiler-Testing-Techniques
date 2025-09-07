
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear()(x1)
        v2  = v1 + other
        v3  = torch.nn.functional.relu(v2)
        return v3
 
# Initializing the model
m = Model()

