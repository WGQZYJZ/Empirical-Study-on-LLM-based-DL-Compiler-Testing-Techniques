
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = self._linear(x1)  # Pass the input through the first layer (called _linear in PyTorch API).
        return self._linear(v.permute(0, 2, 1))  # Permute the output tensor to the order of weight/bias

    def _linear(self, x):  # Define new function to be called from forward function when calling 'forward' function
        ...


# Initializing the model
m = Model()

