
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply linear transformation to the input tensor
        v2 = v1 - other 
        return relu(v2)


# Initializing the model