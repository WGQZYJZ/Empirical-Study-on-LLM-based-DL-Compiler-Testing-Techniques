
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        v1 = torch.mm(inp1, inp2) # 1
        v2 = v1 + inp  # 2
        return v2


# Initializing the model
m  = Model()
__output_v1__, __output_v2__, __output_v3__ = m(**{inp1,inp2})

