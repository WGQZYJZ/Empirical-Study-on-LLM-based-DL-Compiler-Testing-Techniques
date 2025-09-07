
class Model(torch.nn.Module):
    def __init__(self, num_units=128):
        super().__init__()
        self.linear = torch.nn.Linear(10 * 3 * 64 * 64, num_units)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, self.conv1.weight, x2) # Matrix multiplication and add
        v2 = torch.cat([v1], dim=0) # Concatenate along dimension 0 to produce a tensor of shape (24576, 128)
        v3 = torch.nn.functional.relu(self.linear(v2)) # Linear activation followed by ReLU
        return v3


# Initializing the model
m = Model()


x1 = torch.randn(10 * 3 * 64 * 64) # shape=(24576, 10*3*64*64)
x2 = torch.randn(10 * 3 * 64 * 64) # shape=(24576, 10*3*64*64)
