
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.7071067811865476 # Subtract '0.7071067811865476' from the output of the linear transformation
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()


