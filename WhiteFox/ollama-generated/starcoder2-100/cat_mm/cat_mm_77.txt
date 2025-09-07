
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        v1  = v / torch.std(v).item() 
        v2  = v + v + v
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
  x1 = torch.randn(3, 7)
  x2 = torch.randn(7, 8)
 