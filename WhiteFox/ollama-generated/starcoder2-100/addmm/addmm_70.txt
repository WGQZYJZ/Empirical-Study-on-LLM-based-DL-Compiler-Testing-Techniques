
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1):
        v1 = torch.mm(inp1)
        v2  = v1 + v1
        return v2

 # Initializing the model with input tensor
i1_tensor = torch.randn(4, 5).float()
m  = Model()
  