
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 2  # Subtract 'other' from the output of the linear transformation
        v2 = torch.relu(v1)  # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m = Model()


