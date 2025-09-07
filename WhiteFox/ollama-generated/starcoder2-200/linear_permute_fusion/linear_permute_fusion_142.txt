
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(30, 5)

    def forward(self, x1): 
        v2  = self.linear1(x1) # Apply linear transformation to the input tensor firstly

        return v2.permute(1, 2, 0).contiguous()


# Initializing the model
m  = Model()


# Inputs to the model:
x1 = torch.randn(3, 5, 30) 
 