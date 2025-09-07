
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1.shape[0], 1], 1)
        t2 = convert_element_type(t1, dtype=torch.float32)
        t3 = torch.cumsum(t2, dim=1)
        return t3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(64, 3, 64, 64)
x2 = torch.randn(64, 3, 64, 64)
