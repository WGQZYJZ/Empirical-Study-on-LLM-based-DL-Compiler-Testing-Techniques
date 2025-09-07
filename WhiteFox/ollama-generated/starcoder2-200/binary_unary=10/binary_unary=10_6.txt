
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3200, 198)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3


# Initializing the model and setting random seed for reproducible results
m = Model()
torch.manual_seed(42)  # Set fixed random seed
 
# Inputs to the model
x1 = torch.randn(1, 3200)
other = torch.randn(198,)


# Initializing the model with random weights
model = Model()
torch.manual_seed(42)  # Set fixed random seed for reproducible results
m(x1).detach().numpy() # The model is executed and a numpy array is obtained by converting the output to a numpy array using `.detach()`

