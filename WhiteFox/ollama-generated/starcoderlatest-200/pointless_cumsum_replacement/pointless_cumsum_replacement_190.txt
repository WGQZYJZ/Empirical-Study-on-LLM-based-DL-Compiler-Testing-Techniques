
class Model(torch.nn.Module):
    def __init__(self, n1: int, dtype: torch.dtype = None):
        super().__init__()
        self.t1  = torch.full([n1, 2], 1, dtype=dtype)
        self.convert_element_type()
 
    def forward(self):
        t3 = torch.cumsum(self.t2, 1)
 
    def convert_element_type(self):
        self.t2  = torch.convert_element_type(self.t1, dtype=torch.float64)


# Initializing the model
m = Model()
# Inputs to the model
# 