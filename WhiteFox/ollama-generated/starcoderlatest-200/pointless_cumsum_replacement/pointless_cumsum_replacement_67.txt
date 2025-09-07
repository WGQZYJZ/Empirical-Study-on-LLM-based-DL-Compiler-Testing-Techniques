
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.full([x.shape[0], 1], 1)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)

# Inputs to the model
x = torch.randn(1, 16)
