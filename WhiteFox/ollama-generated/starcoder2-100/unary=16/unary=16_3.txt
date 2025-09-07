
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(3072, 1)
    
    def forward(self, x):
        v1 = self.lin(x)
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
v2 = torch.randn(64, 3072) # random inputs to the model (e.g., 64 3-D tensors of size 8 x 8 x 128)


