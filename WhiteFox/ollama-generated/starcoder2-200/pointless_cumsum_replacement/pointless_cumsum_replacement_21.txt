
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([256, 3072], 1, dtype=torch.float32) # 256: arg1, 3072: arg2
        v2  = torch.tensor(v1).convert_element_type(dtype=torch.float64)
        v3  = torch.cumsum(v2, dim=1) 
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = 0
