
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.size(0), 1], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)

# Inputs to the model
x1 = torch.randn(10, dtype=torch.float32, device='cuda:0')
