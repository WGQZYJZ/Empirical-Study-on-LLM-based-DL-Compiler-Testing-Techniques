
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None):
        if other:
            v2 = self.linear(x1) + other # Apply linear transformation to input tensor and add it with `other` keyword argument
        else: 
            v2 = self.linear(x1) # Apply linear transformation to input tensor without adding anything
        v3 = torch.nn.ReLU()(v2)  # Apply ReLU activation function to output of the linear transformation
        return v3
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 m = Model()

 