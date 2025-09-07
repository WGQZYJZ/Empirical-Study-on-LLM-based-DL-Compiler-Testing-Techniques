
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v0  = torch.randn(247956, 3) # The shape of 'v0' is (247956, 3). It is different from the previous one in the same way. 
        v1  = self.linear(x1)
        v2  = v0 - v1

        return v2


# Initializing the model
m = Model()

 # Inputs to the model
v4_shape = (1,3)  # The shape of 'other' is different from that in the previous model.
x1 = torch.randn(1,*v4_shape)
__output__  = m(x1)
