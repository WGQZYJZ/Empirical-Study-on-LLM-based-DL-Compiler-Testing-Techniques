
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input = torch.nn.Linear(128, 512)
 
    def forward(self, x3):
        v7  = torch.tanh(x3)
        return v7


# Initializing the model
m  = TransformerModel()
 
 # Inputs to the model 
 x10   = torch.randn(4, 96 ,5) + 4.
 __output__  = m(x10)
