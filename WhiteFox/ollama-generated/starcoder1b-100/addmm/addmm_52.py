
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.inp = torch.tensor([1], device=inp)
 
    def forward(self, x1, **kwargs):
        return x1 + kwargs["inp"]


