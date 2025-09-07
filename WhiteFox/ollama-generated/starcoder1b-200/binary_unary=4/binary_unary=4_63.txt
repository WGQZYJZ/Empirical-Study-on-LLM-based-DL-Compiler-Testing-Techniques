
class Linear(torch.nn.Module):
    def __init__(self, in_size, out_size, num_layers=2, padding=0, nonlin='ReLU'):
        super().__init__()
 
        # Create a sequential container for the linear transformation (in_size -> out_size)
        self.linear = torch.nn.Linear(in_size, out_size)

        if num_layers == 2:
            # Create a second linear transformation which transforms to ReLU
            self.nonlin = getattr(torch.nn, nonlin)(out_size)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
l  = Linear(in_size=32, out_size=8, num_layers=1)
