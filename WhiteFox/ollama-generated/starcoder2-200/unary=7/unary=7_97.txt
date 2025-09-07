
class Model(torch.nn.Module):
    def __init__(self, in_features):
        super().__init__()
        self.lin = torch.nn.Linear(in_features=64 * 32 , out_features=78)
 
    def forward(self, x1):
        l1 = self.lin(x1)
        l2 = clamp(min=-60., max=l1 + 3.) / 5. 
        return l2


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(8, 47*9).abs().round()
