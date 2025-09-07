
m  = nn.Linear(3,8)
 
# Inputs to the model
x1  = torch.randn(10, 3)
__output__  = m(x1).clone()