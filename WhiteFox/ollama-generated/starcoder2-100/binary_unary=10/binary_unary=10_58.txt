
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Input to the model
x1  = torch.randn(4,50,50).to("cuda")

__output__  = m(x1)
