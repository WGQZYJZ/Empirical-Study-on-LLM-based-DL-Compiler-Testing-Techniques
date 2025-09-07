
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        v1 = x.view(-1, 784) # Flatten the input tensor into a vector
        v2 = self.linear(v1) # Apply the linear transformation to the vector of the input tensor
        return torch.relu(v2)


# Initializing the model
m = Model()


