
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t3 = torch.full([arg1, arg2], 1, dtype=dtype)
        t4 = convert_element_type(t3, dtype) 
        t5 = torch.cumsum(t4, 1)
        return t5
# Initializing the model
m = Model()


