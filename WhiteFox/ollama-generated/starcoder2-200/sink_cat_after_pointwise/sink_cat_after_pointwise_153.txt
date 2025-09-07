
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1  = torch.cat([x1, x1], dim=0)
        t2 = t1.view(-1, 1).clone() # Clone the tensor
        t3 = torch.nn.functional.relu(t2) # Apply ReLU to the reshaped clone of t2

        return (None,)

# Initializing the model
m = Model()

