
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1): 
        output = torch.nn.functional.dropout(input1, 0.5)
        return torch.rand_like(output, dtype=torch.float32), self.weight


# Initializing the model
m = Model()


# Inputs to the model
input1  = torch.ones((8,))

