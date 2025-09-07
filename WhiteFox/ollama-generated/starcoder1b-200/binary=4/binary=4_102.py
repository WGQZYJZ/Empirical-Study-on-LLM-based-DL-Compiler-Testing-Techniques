
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 20)
 
    def forward(self, x1):
        return self.linear(x1) + 1

 # Initializing the model
m = Model()
 
 # Inputs to the model
input_tensor = torch.randn(1, 100)
