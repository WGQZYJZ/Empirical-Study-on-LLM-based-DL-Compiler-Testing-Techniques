
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(24 * 8 * 8, 3)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = torch.nn.functional.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(4, 8 * 8 * 3)
__output__= m(x1)

