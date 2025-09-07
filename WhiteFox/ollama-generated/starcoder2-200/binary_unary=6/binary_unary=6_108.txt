
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(28, 64, bias=True)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2 = v1 - other # Substracts 'other' from the output of linear transformation
        v3 = torch.relu(v2) # Applies the ReLU to the result (after subtraction) 
        return v3


# Initializing the model
m  = Model()

# Inputs for the model
x1=torch.randn(4, 6000).view(-1, 784) # This model takes a matrix of size [4, 28, 28]
