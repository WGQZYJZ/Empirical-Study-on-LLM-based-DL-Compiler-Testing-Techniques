
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Applying linear transformation to the input tensor
        return v1 + other


# Initializing model and passing a keyword argument as a tensor to the model for inference.
m = Model()
other  = torch.rand(3)
