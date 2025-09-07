

class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
       v1  = self.conv(x1) 
       return v1 + other


# Initializing the model:
m_no  = Model(None) # The input is a single argument
m_yes = Model(other  = torch.randn(1)) 

# Inputs to the model:
x1   = torch.randn(1,3,64,64)

__output__  = m_no (x1) # This call must generate the output using a single argument
__output2__ = m_yes(x1) # This call must generate the output using two arguments
