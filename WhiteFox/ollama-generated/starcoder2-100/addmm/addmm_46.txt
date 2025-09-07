
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(25, 10)
        self.add = torch.add
 
    def forward(self, inp):
        v1 = self.matmul(inp[:, :25]) # Perform linear transformation on a first 25 columns of the input tensor 'inp'
        return self.add(v1, self.__input__)
 
# Initializing the model and feeding a dummy input
m  = Model()
