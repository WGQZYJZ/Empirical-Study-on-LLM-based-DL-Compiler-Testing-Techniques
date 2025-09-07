
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.nn.functional.linear(x1.permute(0, 2, 1), 4, 5) 
        v2a = torch.bmm(v1.permute(0, 2, 1), x2).permute(0, 2, 1)
        return v2a


# Initializing the model
m  = Model()
__output__  = m(x1, x2)