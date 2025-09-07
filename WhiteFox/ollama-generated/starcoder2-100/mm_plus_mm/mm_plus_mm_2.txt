
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1  * t1 + torch.randn(10, 14) # Here is where we assume that t1 is already defined. But since this is an added tensor, we will add it after multiplication by the constant. 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(300, 8)
t1 = torch.randn(7, 5)
