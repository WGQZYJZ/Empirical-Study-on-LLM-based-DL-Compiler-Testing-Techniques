
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
    
    def forward(self, x1, x2): 
        # linear transformation is applied to the input tensors and then 'other' is subtracted from their output.
        # here, 'x2' is the variable that was defined outside of the model definition above, so it will be used for the second parameter in the function call. 
        v1 = self.linear(x1)  
        v3  = x2 - other
        return v1, v3

# Initializing the model
m = Model()

