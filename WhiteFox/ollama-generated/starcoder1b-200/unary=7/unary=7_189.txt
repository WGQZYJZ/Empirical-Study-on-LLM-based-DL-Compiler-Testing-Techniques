
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
        # This is a parameter to the model
        # that can be modified by the optimizer. 
        self.clamp_min = torch.tensor(0.)
        self.clamp_max = torch.tensor(6.)
 
    def forward(self, x1):
        v1 = self.linear(x1) * self.clamp(torch.min=0., max=6., l1  + 3) / 6
        return v1


# Initializing the model
m = Model()


