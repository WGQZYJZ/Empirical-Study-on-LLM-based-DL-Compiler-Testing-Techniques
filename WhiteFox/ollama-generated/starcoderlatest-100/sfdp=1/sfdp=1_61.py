
class Model(torch.nn.Module):
    def __init__(self, dim1: int, dim2: int):
        super().__init__()
        self.linear = torch.nn.Linear(dim1 * dim2, dim2)
 
    def forward(self, x):
        x = x.view(-1, 4 * 9 * 9) # Flatten the tensor into a vector
        v1 = self.linear(x)
        return v1


# Initializing the model
m = Model(32768, 1024)

