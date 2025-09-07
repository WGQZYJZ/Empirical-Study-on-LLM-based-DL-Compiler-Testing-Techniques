
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2560, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + __other__ # The keyword argument "other" is used for the 3rd input of torch.add
        return v2


# Initializing the model
m = Model()


# Inputs to the model (specified by the keyword argument "other")