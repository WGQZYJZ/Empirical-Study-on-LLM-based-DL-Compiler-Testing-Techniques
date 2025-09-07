
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):

        # Scenario A
        v3 = torch.nn.functional.linear(
            torch.bmm(x1, x2), self.linearA.weight)


        return v3


# Initializing the model
m  = Model()

# Inputs to the model. The input tensors should be different from their  previous counterparts.
x1 = torch.randn(4, 6, 8) # A new tensor with different size than previous. Also, please don't generate tensors with the size larger than the specified one in requirements.
x2 = torch.randn(4, 7) # A new tensor with different size than previous. Also, please don't generate tensors with the size larger than the specified one in requirements.

