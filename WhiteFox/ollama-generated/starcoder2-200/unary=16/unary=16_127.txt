
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*70, 81)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = F.relu(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model (assuming you know the size of input tensors that you need to feed in the model)
x  = torch.randn(4, 256*70)

 # Outputs from the model (assuming the output of the model is a probability distribution with 81 classes)
__output__  = m(x)

