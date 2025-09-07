
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1)
        t2 = convert_element_type(t1, dtype=torch.int32)
        t3 = torch.cumsum(t2, dim=0)
        return t3


# Initializing the model
m = Model()
