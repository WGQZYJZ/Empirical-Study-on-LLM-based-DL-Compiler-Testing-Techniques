
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 - other_variable
        v3 = F.relu(v2)   
        return v3


# Initializing the model with random weights and biases
m  = Model()
torch.manual_seed(42) # Fixing the seed to ensure reproductibility across runs
m.linear.weight[:] = torch.randn(10, 32).mul_(1e-5)
m.linear.bias[:] = torch.zeros(10)


# Inputs to the model
x1  = torch.randn(4, 32) # This is not the input of the ReLU activation function! 
