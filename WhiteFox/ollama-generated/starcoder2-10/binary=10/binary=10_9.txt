
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = torch.nn.functional.linear(x1) 
        v2 = v1 + other
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(3072, 1536)  # Input tensor
other = torch.randn(1536, )   # Tensor with shape [batch_size x 1]
