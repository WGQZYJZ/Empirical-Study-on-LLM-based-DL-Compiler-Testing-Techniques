
class Model(torch.nn.Module):
    def __init__(self, n_list=3):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * n_list, dim=-1) # Concatenation of the result tensor along a certain dimension
        return v2

# Initializing the model with 4 layers as default and number of layers to 3 (mimicking the previous example).
m  = Model(n_list=3)

 # Inputs to the model