
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) # linear transformation with input_size=3 and output size=8 
        v2 = torch.tanh(v1) # applying hyperbolic tangent function to the output of linear transformation, which is 8 in dimension
        return v2

# Initializing the model
m = Model()

