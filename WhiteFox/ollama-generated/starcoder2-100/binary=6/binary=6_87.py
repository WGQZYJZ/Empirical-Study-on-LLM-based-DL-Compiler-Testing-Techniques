

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,8)
 
    def forward(self, x1):
        v2  = self.linear(x1)
        return v2 - other


# Initializing the model with initial value of 'other'
other = 0
m_without_other = Model()
 
# Inputs to the model without 'other' specified. 'other' is not used in forward function since it is not passed as argument.
x1 = torch.randn(2,3)
__output___without__other__ = m_without_other(x1)

 # Initializing the model with initial value of 'other'
other  = 4567890
m_with_other  = Model()
 
# Inputs to the model with 'other' specified. 'other' is used in forward function as argument.
x2 = torch.randn(3,4)
__output___with__other__ = m_with_other(x1, other=other)

 # Model should have a total of 7 parameters in it and all of them are trainable.

p0 = 3
p1 = 8
p2 = torch.nn.Linear(3, p1).state_dict()
p3 = torch.randn((4567890))

 # Model should have a total of 3 gradients.
g1 = 5.4e-03
g2 = g3  = -g1 
