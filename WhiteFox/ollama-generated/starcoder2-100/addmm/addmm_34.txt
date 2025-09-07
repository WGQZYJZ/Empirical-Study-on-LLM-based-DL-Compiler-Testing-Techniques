
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2=None):
        t1 = torch.mm(inp1, self.weight)  # Matrix multiplication operation on two input tensors 
        if inp2 is not None:
            t2 = t1 + self.bias_vector
        else: 
            t2 = t1  # If the 2nd input tensor does not exist then use the first input as a 6-dimensional vector
        return t2


# Initializing the model and passing the input tensors to forward() function
m  = Model(weight=torch.randn(5, 4), bias_vector=torch.randn(3))
