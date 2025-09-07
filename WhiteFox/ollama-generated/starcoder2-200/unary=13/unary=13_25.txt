
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        return v1 * v2


# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor  = torch.randn(5, 784)
 
# Initializing a random seed for PyTorch tensors (for reproduction of results)
torch.manual_seed(403192659)
  