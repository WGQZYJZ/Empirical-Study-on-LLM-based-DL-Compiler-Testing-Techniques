
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        v3 = torch.full([5, 4], 1) + torch.full([5, 4], 2) # Create two tensors filled with the scalar value 1 and then fill them in with the scalar value 2
        return v3

# Initializing the model
m = Model()


