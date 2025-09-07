
class Model(torch.nn.Module):
    def __init__(self, num_layers: int = 2):
        super().__init__()
        self.num_layers = num_layers
 
    def forward(self, input1):
        for i in range(0, self.num_layers):
            v1 = torch.matmul(input1, input2)
            t1 = torch.cat([v1, v1, ..., v1])
        return t1


# Initializing the model with different numbers of layers
m = Model() # num_layers = 3
m = Model(num_layers=5) # num_layers = 2
