
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4, 8)
    
    def forward(self, x):
        v0 = F.softmax(x + 3, dim=2) 
        v1 = self.linear1(v0[:, :, :5])  # Apply linear transformation to the input tensor
        v2 = torch.clamp_max_(torch.mul(v1[0], v0), 6) # Clamp the maximum value of the output of the linear transformation to `6`
        v3 = torch.div(v2, 5.) # Divide the maximum value of the clamped output by 5
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8)
__output__  = m(x1)

