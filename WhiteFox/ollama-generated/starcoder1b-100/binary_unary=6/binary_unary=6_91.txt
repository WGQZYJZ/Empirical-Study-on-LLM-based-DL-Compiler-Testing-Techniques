
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 20)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 50 # Subtract value 50 from the output of the linear transformation
        v2 = relu(v1) # Apply the ReLU activation function to the result
        return v2


# Initializing the model
m = Model()

