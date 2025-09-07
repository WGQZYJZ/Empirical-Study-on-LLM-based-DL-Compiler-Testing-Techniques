
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(256, 1)
 
    def forward(self, x1):
        v1 = t1 + mat1 # Add a constant and then perform a matrix multiplication of mat1 and mat2 and add it to the input tensor
        v2 = torch.cat([v1], dim)
        return self.fc(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8)
