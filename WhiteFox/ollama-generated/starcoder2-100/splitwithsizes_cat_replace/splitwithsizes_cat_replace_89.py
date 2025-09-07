
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        split_tensors  = torch.split(x1)
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
 
 __output__= m(x1)

