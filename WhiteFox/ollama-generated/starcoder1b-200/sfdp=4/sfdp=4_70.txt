
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(64 * 5 * 5, 20)
        self.fc2 = torch.nn.Linear(20, 10)
 
    def forward(self, x):
        # Get the features of the model (output of the layer defined above) and compute them
        v1 = self.fc1(x)
        v2 = self.fc2(v1)
 
        # Scale and shift the logits to the range [-1, 1]
        v2_scale = torch.exp(v2 - max(v2))
        v2_shift = max(v2) + 1e-6 - v2
        output = (v2_scale * v2_shift).log()  # log it so that values will be in [0, inf]
 
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 64, 5, 5)
