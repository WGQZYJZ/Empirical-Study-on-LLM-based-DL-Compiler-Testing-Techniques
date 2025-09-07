
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        
t2  = torch.relu(x1)
        return t2

# Initializing the model
m = Model()


# Inputs to the model