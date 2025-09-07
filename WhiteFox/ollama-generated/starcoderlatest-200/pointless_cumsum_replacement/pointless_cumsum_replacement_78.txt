
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([x1.shape[0], 8, x1.shape[-2], x1.shape[-1]], 1)
        v2 = convert_element_type(v1, torch.float32)
        v3 = torch.cumsum(v2, 1)
        return v3
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
