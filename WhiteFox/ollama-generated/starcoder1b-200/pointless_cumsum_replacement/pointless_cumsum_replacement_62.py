
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, t2=None):
        t3 = convert_element_type(x1, torch.float)
        return torch.cumsum(t3, 1)


# Inputs to the model
__input__ = torch.randn([10, 3, 8, 8])
x2 = Model()(__input__)

