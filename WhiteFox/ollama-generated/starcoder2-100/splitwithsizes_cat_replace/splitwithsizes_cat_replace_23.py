
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 56000, dim=2) # Split the input tensor into two tensors along dimension 2 with size 56000 each
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))],dim=2) # Concatenate these split tensors along dimension 2 to produce a single tensor
        return concatenated_tensor

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3,64000,907)
__output__  = m(x1)

