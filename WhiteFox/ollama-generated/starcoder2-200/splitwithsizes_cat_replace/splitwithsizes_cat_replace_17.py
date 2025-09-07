
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.split(x1, 32, dim=0) # Split the input tensor into several tensors along dimension 0 with size 32
        c = torch.cat([i for i in range(len(v))], dim=0) # Concatenate these split tensors back into one big tensor using 'torch.cat'

# Initializing the model
m  = Model()

# Input to the model
x1 = torch.randn(5, 32 * 48)

