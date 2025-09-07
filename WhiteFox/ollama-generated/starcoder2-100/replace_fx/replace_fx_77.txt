
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.5) # 50% dropout
        v2 = torch.rand_like(v1, out=None) # Generate a tensor with the same size as input filled with random numbers (can use randperm or other methods to implement)
        return [v1, v2]

# Initializing the model
m  = Model()

