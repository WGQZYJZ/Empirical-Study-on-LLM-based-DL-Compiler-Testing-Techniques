
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28, 10)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = torch.clamp_(x1, min=self.min_value)  # Clamp the input to a minimum value
        v2 = torch.clamp_(v1, max=self.max_value)  # Clamp the output of the previous operation to a maximum value
        return self.linear(v2)


# Initializing the model
m = Model()


