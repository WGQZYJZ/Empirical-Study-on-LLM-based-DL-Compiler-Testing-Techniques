
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope
        return torch.where(v2, v1, v3)


m = Model()
__output__  = m(torch.randn(5))

# Initializing the model
m  = Model()
 
 # Inputs to the model
x1 = torch.tensor([[-0., -7.], [64.,  9.]], requires_grad=True)
 