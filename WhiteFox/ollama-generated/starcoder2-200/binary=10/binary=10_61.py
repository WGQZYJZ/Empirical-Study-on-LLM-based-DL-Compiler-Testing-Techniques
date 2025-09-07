
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + other_tensor # Add the input tensor to another tensor specified by "other"
        return v2


# Initializing the model
m  = Model()
other_tensor = torch.randn(3,8) # Create a random tensor with size [3,8]

# Inputs to the model
x1  = torch.randn(10,3)
__output__  = m(x1)

