
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.empty([32768, 4], dtype=torch.float)
        v1 = convert_element_type(v0, torch.int8)
        v2 = torch.cumsum(v1, 1)
        return v2


# Initializing the model and obtaining its output tensor
m = Model()
o1 = m(input1)
 