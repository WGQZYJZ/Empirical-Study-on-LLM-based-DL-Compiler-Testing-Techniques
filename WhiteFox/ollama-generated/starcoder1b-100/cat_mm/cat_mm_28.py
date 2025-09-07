
class Model(torch.nn.Module):
    def __init__(self, cat_dim=1):
        super().__init__()
        self.cat = torch.nn.AdaptiveAvgPool2d((64,))
 
    def forward(self, x):
        v  = self.cat(x)
        return v

# Initializing the model
m = Model()

