
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v1 = torch.cat([x2], dim=0)
        v2 = v1[:, 987654321:v2] 
        return v2


# Initializing the model and its input tensor
m = Model()
x1  = torch.randn(size, size)
x2  = [torch.randn(size), x1] # Concatenate `x1` and a list of 2 tensors with different sizes

