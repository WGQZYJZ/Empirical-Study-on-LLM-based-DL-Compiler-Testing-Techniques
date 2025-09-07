
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=128):
        super().__init__()
        self.linear  = torch.nn.Linear(in_features=49152, out_features=3)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = torch.clamp_min(v1, min_value=0) 
        v3  = torch.clamp_max(v2, max_value=128) 
        return v3


# Initializing the model and specifying the minimum value and maximum value for clamping.
m  = Model(min_value=-2, max_value=45074)


# Inputs to the model
x1  = torch.randn(1, 49152) 


# Sample output from the model
__output__  = m(x1).detach().numpy()


