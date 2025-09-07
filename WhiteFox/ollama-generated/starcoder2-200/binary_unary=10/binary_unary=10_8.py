
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear0(x1) + torch.tensor([[4.], [5.]])
        v2  = torch.relu(v1)
        return v2

 # Initializing the model
m  = Model()
 
# Inputs to the model 
 x1  = torch.randn(3, 6400)
 
 # Calculating the output of the model
 __output__  = m(x1)
