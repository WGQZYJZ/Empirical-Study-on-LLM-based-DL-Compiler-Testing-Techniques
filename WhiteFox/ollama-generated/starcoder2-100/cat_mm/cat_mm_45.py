
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2)
        v2  = torch.cat([v1] * 3000, dim=0) # Concatenate the result tensor along dimension 0 3000 times
        return v2

# Initializing the model
m  = Model()

