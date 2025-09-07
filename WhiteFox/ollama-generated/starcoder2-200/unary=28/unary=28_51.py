
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        # linear layer
        v1  = torch.randn(4,5)
        v2  = v1 * min_value
        v3  = v2 + max_value
        return v3


# Initializing the model
m  = Model()
__output__  = m(torch.randn(4))

