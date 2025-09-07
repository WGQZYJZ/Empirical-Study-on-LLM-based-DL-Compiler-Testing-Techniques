
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = v1 + self.__other__ 
        return v2

# Initializing the model with the keyword argument __other__ set to some non-zero tensor
m  = Model()
m.__other__ = torch.ones(4, 5).requires_grad_()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
 # Initializing the model with the keyword argument __other__ set to some non-zero tensor and computing its gradient
with torch.enable_grad():
    m.__other__ = torch.ones(4, 5).requires_grad_()
    __output1__ = m(x1)
__gradient1__  = torch.autograd.grad(__output1__, [m.__other__], retain_graph=True)[0]
 
 
 # Initializing the model with the keyword argument __other__ set to some non-zero tensor and computing its gradient on a new input value x2
with torch.enable_grad():
    m.__other__ = torch.ones(4, 5).requires_grad_()
    __output1__ = m(x1)
    __output2__ = m(torch.randn(1, 3, 64, 64))
 
__gradient1__, __gradient2__  = torch.autograd.grad(__output1__, [m.__other__], retain_graph=True)[0]


