
class Model(torch.nn.Module):
    def __init__(self, min_value=None, max_value=-100.):
        super().__init__()
        self.linear  = torch.nn.Linear(256*7*7 , 4)
 
    def forward(self, x1):
        v1  = self.linear(x1).reshape(-1,  8, 3, 9, 9)
        v2  = torch.clamp_min(v1, min_value=0.)
        v3  = torch.clamp_max(v2, max_value=-15.)

        return v3


# Initializing the model