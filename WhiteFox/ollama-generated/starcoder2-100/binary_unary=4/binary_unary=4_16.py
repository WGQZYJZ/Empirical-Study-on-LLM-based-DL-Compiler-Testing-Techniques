
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         return self.linear(x1)

    @staticmethod
    def linear():
        # Please implement a function that creates a `torch.nn.Linear` layer and returns it.
        pass


# Initializing the model
m  = Model()


# Inputs to the model
__input__  = torch.randn(5, 4) # This is an input tensor that is not used by your code at all.


# Outputs of the model: The function call of your `linear()` is evaluated during compilation
output1_1  = m(__input__)
output2_1  = output1_1 + __input__
output3_1  = F.relu(output2_1)