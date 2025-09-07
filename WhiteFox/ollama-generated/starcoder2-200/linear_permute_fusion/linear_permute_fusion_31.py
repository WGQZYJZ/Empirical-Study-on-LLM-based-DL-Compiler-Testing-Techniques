
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
       v1 = input_tensor[:, :, 0] 
       v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)

       return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(256, 4, 8).to('cpu')
__output__  = m(x1)


