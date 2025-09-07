
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(832, 512)
 
    def forward(self, x1):
        v0 = x1.detach()
        v1  = self.linear(v0) 
        v4  = torch.tanh(v1 - 976.406) # Subtract 976.406 from the result of applying a linear transformation to an input tensor
        return torch.relu(v4)


# Initializing the model
m  = Model()
 
# Inputs to the model
x2 = torch.randn(1, 832)
