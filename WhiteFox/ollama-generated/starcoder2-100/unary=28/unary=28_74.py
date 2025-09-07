
class Model(torch.nn.Module):
    def __init__(self, maxvalue=0, minvalue=-128, biasflag=True):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 7) # the number of input features should match those of the input tensor
        if not biasflag:
            self.linear.bias = None
        
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.clamp_min(v1, minvalue=0) # the minimum value is 0
        v3 = torch.clamp_max(v2, maxvalue=-1) # the maximum value is -1
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3 * 64 * 64).to('cpu') 

