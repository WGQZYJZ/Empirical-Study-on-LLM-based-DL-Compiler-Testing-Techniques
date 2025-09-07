
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = torch.cat([v1, x3], dim=1)
        return v2


# Inputs to the model
input_tensors = [
    torch.randn(8), # Tensor1
    torch.randn(64), # Tensor2
    torch.randn(3) # Tensor3
  ]
