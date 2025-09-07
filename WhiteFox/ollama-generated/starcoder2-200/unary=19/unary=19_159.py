
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        v0 = self.linear(x1) # Apply a linear transformation to the input tensor 
        v1 = torch.sigmoid(v0)# Apply the sigmoid function to the output of the linear transformation
        return v1

# Initializing the model
m  = Model()

