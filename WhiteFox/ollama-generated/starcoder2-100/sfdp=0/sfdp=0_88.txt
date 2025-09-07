
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.transformer = torch.nn.TransformerEncoderLayer(
            d_model=32, nhead=4, dim_feedforward=16)
 
    def forward(self, x):
        y  = self.transformer(x)
        return y


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(50, 32, 32)
  __output__  = m(x)

