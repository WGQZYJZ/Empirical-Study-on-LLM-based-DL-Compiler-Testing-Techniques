
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying a linear transformation to an input tensor
        return v1 - other

# Initializing the model with a non-zero tensor for 'other'
m  = Model()

