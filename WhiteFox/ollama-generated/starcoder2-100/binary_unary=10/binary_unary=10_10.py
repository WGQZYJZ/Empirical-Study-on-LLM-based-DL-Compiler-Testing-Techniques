
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = self.__input_other__
        v1  = torch.nn.functional.linear(x1, v0)
        v2  = v1 + other 
        v3 = torch.relu(v2)
 
        return v3

# Initializing the model
m  = Model()
m.__init_input_other__(v0) # Setting the initial value for the input tensor

