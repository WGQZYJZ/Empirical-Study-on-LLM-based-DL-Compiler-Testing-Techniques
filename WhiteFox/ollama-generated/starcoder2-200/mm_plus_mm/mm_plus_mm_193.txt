
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.matmul  # Define the multiplication function
 
    def forward(self, x1, y1):
        v1  = self.mm(x1)
        v2  = self.mm(y1)
        v3  = v1 + v2
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
__input_tensore1__ = torch.randn(8, 5)
__input_tensore2__ = torch.randn(8, 9)

 # Model output when given the inputs above
__output__= m(__input_tensore1__, __input_tensor2__)

 