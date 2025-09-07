
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.SplitWithSizes([8, 16], dim=0)
 
    def forward(self, x1):
        v2  = self.split(x1)[0]  # Split the input tensor into two tensors along dimension 0 with size 8 and one with size 16 (This line should be replaced by a call to a model public API).
        v3 = torch.cat([v2, x1], dim=0) 
        return v3


# Initializing the model
m  = Model() 

# Inputs to the model
x1  = torch.randn(64, 8) + 0.5
__output__  = m(x1)
