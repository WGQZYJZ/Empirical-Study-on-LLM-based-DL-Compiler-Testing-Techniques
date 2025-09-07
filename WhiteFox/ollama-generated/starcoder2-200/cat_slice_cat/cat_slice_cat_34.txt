
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, x2):
      v1 = torch.cat([x1, x2], dim=0) # Concatenate the first tensor and the second tensor along dimension 0 (batch size axis).
      return v1


m  = Model() 

# Inputs to the model
x1 = torch.randn(3, 64, 64)
