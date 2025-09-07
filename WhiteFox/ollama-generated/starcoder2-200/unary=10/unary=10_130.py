
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3 # Apply a linear transformation to the input tensor and add 3 to the output of this operation.
        v2 = torch.clamp_min(v1, 0) # Clamp the output of the addition operation to a minimum value of 0.
        v3 = torch.clamp_max(v2, 6)# Clamp the output of the previous operation to a maximum value of 6.
        return v3 / 6
 
# Initializing the model
m = Model()

 # Inputs to the model. x1 has shape [batch size]
x1 = torch.randn(10, 32)
 
 