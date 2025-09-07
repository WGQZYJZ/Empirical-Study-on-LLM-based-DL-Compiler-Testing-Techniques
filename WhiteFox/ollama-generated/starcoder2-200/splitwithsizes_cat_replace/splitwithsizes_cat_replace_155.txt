
class Model(torch.nn.Module):
    def __init__(self, n_input=32, split_sizes=(8)):
        super().__init__()
        self.split = torch.nn.Conv2d(n_input, 8*len(split_sizes), 1)

    def forward(self, x1): 
        splt = self.split(x1).reshape(-1, len(split_sizes))
        return torch.cat([splt[i] for i in range(len(split_sizes))], dim=0)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8,32,64,64) # Replace this line with the line you generated in the previous part of this exercise. 
