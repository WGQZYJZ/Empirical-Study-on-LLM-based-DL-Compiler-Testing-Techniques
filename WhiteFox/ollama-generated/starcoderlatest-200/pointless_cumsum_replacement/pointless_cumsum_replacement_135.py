
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.full([x1.shape[0], 1], 1, dtype=dtype, layout=layout, device=device)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3
 
 # Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(10, 64, 3, dtype=torch.float64, layout=torch.strided, device='cuda', pin_memory=True)
 x2 = torch.ones(x1.shape, device=device)
 x3 = torch.zeros(x2.shape[0], 1, dtype=torch.double, layout=torch.sparse, device='cuda')

 