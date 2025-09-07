
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.mm = torch.nn.functional.linear(input1, input2)
 
    def forward(self, x1):
        v1  = self.mm(x1)
        v2  = torch.cat([v1] * [3] + [v1], dim=0) # Concatenate the result tensor along a specified dimension.
        return v2

# Initializing the model
m = Model()

