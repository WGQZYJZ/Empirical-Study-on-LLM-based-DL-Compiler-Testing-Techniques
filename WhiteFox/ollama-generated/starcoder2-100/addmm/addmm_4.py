
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1, inp2=None):
        if inp2 == None:
            inp = 5 # Assigning a default value to 'inp' for the purpose of this exercise
        else: 
            print("No default for input parameter 2.") # Printing message to the user
            v3 = torch.mm(inp1, inp)
            return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(64, 64).requires_grad_()
