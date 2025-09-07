
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation
        return v2 * 0


# Initializing the model and inputs to it