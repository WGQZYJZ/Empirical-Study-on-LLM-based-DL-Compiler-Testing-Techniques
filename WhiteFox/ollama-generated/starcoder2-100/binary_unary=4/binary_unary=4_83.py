
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1,  other = torch.ones_like(x1))
        v2  = v1 + 0.5
        v3  = relu_(v1) # Replace relu function with a custom ReLU activation function (e.g., using pytorch/torchgen)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
