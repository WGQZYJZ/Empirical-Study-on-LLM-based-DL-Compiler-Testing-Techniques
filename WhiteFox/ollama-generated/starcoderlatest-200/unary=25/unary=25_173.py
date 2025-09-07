
class Model(torch.nn.Module):
    def __init__(self, neg_slope: float):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
        # We initialize here so that negative_slope can be used for other computations and can also be saved
        # as a parameter when we save the model to disk.
        self.neg_slope = neg_slope
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 > 0
 
        v3 = torch.where(v2, v1, -self.neg_slope * v1)
 
        return v3

 # Initializing the model
m = Model(-0.1)
 
 # Inputs to the model
 x = torch.randn(1, 128, 56, 56)
 