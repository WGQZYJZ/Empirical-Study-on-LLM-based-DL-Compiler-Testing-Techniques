
Inputs to the model
x0  = torch.tensor(5) # An input of shape 1
x1  = x0.expand([3,4])
x2  = (torch.arange(-96, -87).view([-3])) + (torch.arange(100))
__output__  = m((x0, x1, x2))

