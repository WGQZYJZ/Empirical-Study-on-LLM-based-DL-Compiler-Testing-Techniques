
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(10, 4)
 
    def forward(self, x):
        return torch.tanh(self.linear(x))
 
 
model = Model()


# Initializing the model
m  = model
 
# Inputs to the model
input_tensor = torch.randn([20], requires_grad=True)
 
__output__  = m(input_tensor)