
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.full([x1, x2], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device)
        v2 = convert_element_type(v1, x1.dtype)
        v3 = torch.cumsum(v2, 0)
        return v3

# Inputs to the model
x1 = torch.randint(low=-5, high=64, size=(1,), dtype=torch.int64).tolist()[0]
x2 = torch.randint(low=-5, high=64, size=(1,), dtype=torch.int64).tolist()[0]
