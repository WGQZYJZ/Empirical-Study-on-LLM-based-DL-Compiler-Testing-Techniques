
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other):
        v2 = torch.nn.functional.linear(x1, self) + other 
        return  relu(v2)


# Initializing the model
m  = Model()
 
# Inputs to the model