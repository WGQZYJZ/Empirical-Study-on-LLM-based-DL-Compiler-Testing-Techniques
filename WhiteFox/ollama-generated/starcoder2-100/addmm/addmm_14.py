
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1: torch.Tensor = None) -> torch.Tensor : # Define forward pass with a default input value of 'inp1' of type 'torch.tensor'
        t1  = torch.mm(inp1[:,None], torch.ones((7,3)).to(inp1))
        t2  = t1 + inp1
        return t2

# Initializing the model
m  = Model()

# Inputs to the model: a 5-dimensional tensor that consists of integers in range [0, 5] and shape (7,3)
inputs = torch.tensor([4., 4., 4., 4., 4., -1., 2]) # Pass input_1 as argument 'inp' with default value 'None'. If it is passed a value, it is of type 'torch.tensor', and its value must be an integer or 0.5.
