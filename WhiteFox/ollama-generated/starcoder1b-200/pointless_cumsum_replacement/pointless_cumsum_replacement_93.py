
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([3, 4], 1, dtype=torch.float32)
        t1 = convert_element_type(v1, torch.uint8)
        v2 = convert_element_type(t1, torch.float64)
        v3 = torch.cumsum(convert_element_type(v2, torch.float32))
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 5, 64, 64)
