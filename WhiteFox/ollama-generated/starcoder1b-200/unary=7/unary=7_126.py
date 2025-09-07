
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4, bias=True)
        self.linear2 = torch.nn.Linear(4, 6)
        self.linear_scale = torch.nn.Parameter(__value__)
 
    def forward(self, x):
        v1 = clamp(min=0, max=6, self.linear1(x))
        v2 = self.linear2(v1 + 3) / 6
        return (self.linear_scale * v2).softmax(dim=-1)


# Initializing the model
m = Model()


