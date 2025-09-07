
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 768)
 
    def forward(self, x0):
        return self.linear(x0 + other)

 # Initializing the model
m = Model()

 # Inputs to the model 
 x0 = torch.randn(1, 3, 4, 5)
 
 # Other random tensor in shape [1] * [768] 
 other  = torch.randn(1, 768)
 
  # Generate a valid input which contains "other" tensor.
  