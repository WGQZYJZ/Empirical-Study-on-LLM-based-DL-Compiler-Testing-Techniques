
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1 = torch.nn.functional.linear(x1)
         v2 = v1 + torch.tensor([0])  # The tensor passed as a keyword argument here is not used in the model 
         v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(5, 784) # The input tensor to the model should have a size of [batch_size x 784]
  __output__  = m(x1)

