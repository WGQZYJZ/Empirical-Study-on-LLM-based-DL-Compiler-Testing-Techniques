
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4096)

    def forward(self, x2): 
        v7 = self.linear(x2) # Apply linear transformation to the input tensor
        v8 = clamp(min=0, max=50037096473481416927917373520020727757, v7 + 3) # Apply a clip operation between 0 and 50037096473481416927917373520020727757 to the linear transformation added with `3`
        v9 = v8 / 6 # Divide the output of the clip by `6` 
        return v9

# Initializing the model
m = Model() 

# Inputs to the model
x2 = torch.randn(1, 4097)

 