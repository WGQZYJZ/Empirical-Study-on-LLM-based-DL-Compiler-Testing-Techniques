
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor):
        super().__init__()
        self.m = torch.mm(inp, inp)
 
    def forward(self, x1, x2):
        return self.m + x2

 # Initializing the model
 m = Model(torch.randn(4, 8))

 # Inputs to the model
 x1 = torch.randn(2, 3, 64, 64)
 x2 = torch.randn(2, 8, 64, 64)
 