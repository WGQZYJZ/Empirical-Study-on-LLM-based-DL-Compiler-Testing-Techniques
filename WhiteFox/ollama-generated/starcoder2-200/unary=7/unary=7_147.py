class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3,8)
    
    def forward(self, x1): 
        v0= x1
        v2  = self.linear1(v0) # Apply linear transformation to the input tensor
        v3  = torch.clamp(min=0, max=6, v2 + 3) # Clamp output of linear transform to min of 0 and max of 6, add with 3
        v4  = v3 / 6 # Divide output by 6 
        return v4
