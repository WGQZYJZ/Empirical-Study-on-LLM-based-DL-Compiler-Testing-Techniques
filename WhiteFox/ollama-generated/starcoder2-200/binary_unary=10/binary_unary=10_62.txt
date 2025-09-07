
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25600, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 800) # Input tensor for the linear transformation layer. Here it is of size 10 x 640 (the dimension before flattening).
other = torch.randn(10, 25600) # Tensor to be added to the output of the linear transformation

 __output__  = m(x1)
 
 
