
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear()(x1) + torch.randn(v1.size()) 
        return v2


# Initializing the model and feeding some random input data to it 
m = Model()
