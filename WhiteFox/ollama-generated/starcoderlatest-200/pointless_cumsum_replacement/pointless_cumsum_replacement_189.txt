
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([10, 4], 1, dtype=x1.dtype) 
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, dim=-1)
        return t3

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(20, 4)
x2 = torch.randn(20, 4).to("cuda:0")
