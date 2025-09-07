
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, inplace=False) # Generate a new tensor filled with dropout value
        v2  = torch.rand_like(v1).cuda() # copy the generated tensor to GPU device and return it as output 
        return v2

# Initializing the model
m = Model().to('cpu')

