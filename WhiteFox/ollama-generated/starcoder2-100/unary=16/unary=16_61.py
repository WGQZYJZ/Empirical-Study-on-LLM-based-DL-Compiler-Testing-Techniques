
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*64*10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = relu(v1)
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
input_tensor  = torch.randn(3048*5, 32, 64, 10)

 # Input_tensor_outout:
input_tensor__output__= m(input_tensor)
