
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 3)
 
    def forward(self, x1):
        v1  = self.linear1(x1) + self._other_tensor # This is a newly added tensor for your model example that does not exist in the previous example.
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model
 x2= torch.randn(3, 20)
 