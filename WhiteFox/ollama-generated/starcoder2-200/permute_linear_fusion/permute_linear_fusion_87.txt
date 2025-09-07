
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1): 
        v1  = x1.permute(0, 3, 1, 4).mean() # Swaps the last two dimensions of an input tensor and then takes its average
        v2  = torch.nn.functional.linear(v1, self.linear.weight)

        return v2

# Initializing the model
m   = Model()


# Inputs to the model:
x1    = 4 * np.random.randn(3072, 96).astype('float32')
