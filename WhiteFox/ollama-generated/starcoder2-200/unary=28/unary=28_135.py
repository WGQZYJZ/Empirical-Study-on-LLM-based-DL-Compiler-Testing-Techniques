
class Model(torch.nn.Module):
    def __init__(self, minv=0., maxv=-128.):
        super().__init__()

        self.linear = torch.nn.Linear(3, 64)

        self.min = minv
        self.max = maxv
 
    def forward(self, x):
        t1  = self.linear(x) # Apply a linear transformation to the input tensor
        t2  = torch.clamp_min(t1, self.min) # Clamp the output of the linear transformation to a minimum value
        t3  = torch.clamp_max(t2, self.max) # Clamp the output of the previous operation to a maximum value
        
        return t3

# Initializing model