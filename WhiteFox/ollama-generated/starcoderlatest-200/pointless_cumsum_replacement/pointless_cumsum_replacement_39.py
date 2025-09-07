
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1], 1, dtype=torch.int64)
        v2 = convert_element_type(v1, torch.int32)
        v3 = torch.cumsum(v2, 0)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randint(1, 64, [1], dtype=torch.int64) # x1 is filled with integer value ranging from 0 to 63
x2 = torch.randint(1, 64, [1], dtype=torch.int64) # x2 is filled with integer value ranging from 0 to 63
