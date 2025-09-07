
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(4, 6)
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1, 4) # Shape (Batch Size x Feature Dimension)
input2 = torch.randn(5, 6) # Shape (Feature Dimension x Hidden Dimension)
input3 = torch.randn(784, 4096) # Shape (Input Data x Hidden Dimensions)
