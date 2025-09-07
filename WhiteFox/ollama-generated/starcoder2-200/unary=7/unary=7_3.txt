
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(8 * 64 **2,1)
 
    def forward(self, x):

        l1  = self.linear(x)
        l2  = l1  * torch.clamp(min=0, max=6, input=l1 + 3) # clamp is used for avoiding exploding values
        l3  = l2 /  6

        return l3

# Initializing the model
m = Model()

 # Inputs to the model

x = torch.randn(4,8 * 64 **2 )

 __output__  = m(x)
