
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1.shape[0], 8], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=False)
        v2 = convert_element_type(v1, x2.dtype)
        v3 = torch.cumsum(v2, 0)
        return v3


# Inputs to the model
x1 = torch.randn(5, 8, dtype=torch.float64, layout=torch.strided, device='cuda:0', pin_memory=False)
x2 = torch.tensor([1.], dtype=torch.float64, device='cpu', pin_memory=False).expand([5, ])
