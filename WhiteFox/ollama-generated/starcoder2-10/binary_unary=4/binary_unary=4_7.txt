
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         y = torch.nn.Linear(x1, 3)(x2) + other
         return self.relu(y)

 # Initializing the model
 m  = Model()
 
# Input tensors for the model
x1  = torch.randn(10, 40) 
other = torch.randn(10, 5).abs() 

# Run the model with different input values and check the output
for i in range(3):
    