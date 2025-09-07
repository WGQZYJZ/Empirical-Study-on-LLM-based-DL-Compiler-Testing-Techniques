
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30,10)
        self.__other__ = 42
        
    def forward(self, x): 
        v1 = self.linear(x) 
        v2 = v1 - self.__other__ # other is not a parameter or a tensor in PyTorch
        v3 = torch.nn.functional.relu(v2) # Replace ReLU with Relu
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4, 30)
__output__  = m(x1)

