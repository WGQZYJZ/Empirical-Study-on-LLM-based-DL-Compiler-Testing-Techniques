
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        v0 = torch.mm(inp1, inp2)  # Perform matrix multiplication on two input tensors 'inp1' and 'inp2', respectively
        v1 = v0 + self._make_constant() 
        return v1

# Initializing the model