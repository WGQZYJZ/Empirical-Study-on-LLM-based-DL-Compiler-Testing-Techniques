

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._convtrans(x1) 
        return torch.tanh(v1)
    
    @staticmethod
    def _convtrans(input_tensor):
       return torch.nn.ConvTranspose2d(in_channels=80, out_channels=96)(
           input_tensor
       )


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,3,50,50)
__output__  = m(x1)