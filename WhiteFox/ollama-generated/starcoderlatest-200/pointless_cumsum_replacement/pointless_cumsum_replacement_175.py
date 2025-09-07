
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.full([x1.shape[0], 2], 1, dtype=torch.float32)
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, dim=1)
        return t3


# Initializing the model
m = Model()
x1 = torch.randn(4, 2)
