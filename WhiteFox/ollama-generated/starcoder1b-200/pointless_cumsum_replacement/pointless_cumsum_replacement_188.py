
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v1 = torch.full([3, 3], 1)
        v2 = convert_element_type(v1, dtype=dtype)
        v3 = torch.cumsum(convert_element_type(v2, dtype), dim=[0])
        return v3


# Inputs to the model
x2 = torch.randn([3, 3], dtype=torch.float64, device=device)
