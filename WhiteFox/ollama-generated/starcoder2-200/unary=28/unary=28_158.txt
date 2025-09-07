
class Model(torch.nn.Module):
    def __init__(self, max_: float = 10., min_= 5.).
        super().__init__()
        self.linear  = torch.nn.Linear()
 
    def forward(self, x2):
        v7  = linear(x2)
        v8  = torch.clamp_min(v7, min_) 
        v9  = torch.clamp_max(v8, max_)
        return v9


# Initializing the model
m1= Model()
m1.