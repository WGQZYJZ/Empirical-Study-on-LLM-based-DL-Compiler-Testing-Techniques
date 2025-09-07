
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1], dim=-1)  # Concatenate input tensors along the last dimension
        v2 = torch.addmm(v1, x2, x2)  # Perform a matrix multiplication of two tensors and add it to the second tensor
        return v2


# Initializing the model
m = Model()

