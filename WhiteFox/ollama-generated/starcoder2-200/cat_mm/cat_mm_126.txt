
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

    def forward(self, x1): # You can refer to input1 as input in __init__ if you want to avoid re-declaring the argument name
        t1 = torch.mm(x1[0], x1[1]) 
        return [t1] * 2 # The length of the list depends on how many times t1 is concatenated

# Initializing the model
m = Model()


__output__  = m(x)  