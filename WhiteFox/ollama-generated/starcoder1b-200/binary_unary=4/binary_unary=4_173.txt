
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
        self.relu    = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        v3 = self.relu(v2)  # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m = Model()


