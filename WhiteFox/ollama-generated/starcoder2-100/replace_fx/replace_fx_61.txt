
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1, self.linear.weight) + \
             torch.nn.functional.dropout(x1, 0.3) # Apply dropout and linear on the input tensor.

        return v2

# Initializing the model
m = Model()

