
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1) + other # add the 'other' tensor to output of linear transformation 
        return nn.functional.relu(v1)


# Initializing the model with keyword argument as input. The input must be a valid PyTorch module (which contains the 'other' tensor). Also, the input must not contain 'other' tensor anywhere else other than in the keyword argument.
m  = Model(other=torch.randn([45])) # pass 'other' to __init__


# Inputs to the model
x1  = torch.randn(30, 10)
