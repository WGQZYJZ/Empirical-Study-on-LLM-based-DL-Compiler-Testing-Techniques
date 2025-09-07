
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...) 
        v2 = torch.rand_like(v1, dtype=torch.float32) # If fallback_random is set to true or if the model is running on CPU device.
        return self.linear(v1, v2)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 5)
