
class Model(torch.nn.Module):
    def __init__(self, arg1=256, arg2=10):
        super().__init__()
        self.t1 = torch.full([arg1, arg2], 1)
 
    def forward(self):
        t2 = convert_element_type(self.t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
