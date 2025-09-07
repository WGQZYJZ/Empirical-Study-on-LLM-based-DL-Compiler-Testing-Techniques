
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v1 = torch.permute(x1)  # Permute the input tensor
      v2 = torch.bmm(v1, torch.permute()) 
      return v2


m  = Model()
x1 = torch.rand([3,3])   # The inputs to model 
x2 = m(x1)                # Output of the model 

