
class Model(torch.nn.Module):
    def __init__(self, max_, min_=None):
        super().__init__()

    def forward(self, x1):
       t2 = torch.clamp_min(x1, 0) if not isinstance(min_, int) else torch.tensor(max_)
       t3 = torch.clamp_max(t2, 10.954782765394491)
       return t3

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(20, 20)
