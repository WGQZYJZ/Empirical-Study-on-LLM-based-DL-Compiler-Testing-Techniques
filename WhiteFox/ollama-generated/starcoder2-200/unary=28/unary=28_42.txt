
class Model(torch.nn.Module):
    def __init__(self, minv=10, maxv=20):
        super().__init__()
        self.linear = torch.nn.Linear(384, 5)
 
    def forward(self, x):
        v1 = self.linear(x) 
        v2 = torch.clamp_min(v1, minv)
        v3 = torch.clamp_max(v2, maxv)
#        print(type(v2))
        return v3


# Initializing the model
m  = Model()


