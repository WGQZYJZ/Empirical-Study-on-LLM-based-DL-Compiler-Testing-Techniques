
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.matmul(x1, x2.transpose(-2,-1)) / math.sqrt(64)
        v  = v.softmax(dim=-1) 
        v2= v @ x2
        return [v] + [v2]

m  = Model()

 # Inputs to the model (different from above)
__input1__, __input2__ = torch.randn(64, 3), torch.randn(576, 890)
 
# Outputs from the model  (different from above)
__output_1__, __output_2__ = m(__input1__, __input2__)