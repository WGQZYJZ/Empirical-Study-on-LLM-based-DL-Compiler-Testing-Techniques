
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 4* 8, 10)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 256 * 4* 8)
 
 # Other tensor that does not exist in the previous one
other_tensor  = torch.randn(10)
 
# Adding the other tensor into the output of the first transformation.
__output__  = m(x1 + other_tensor)

