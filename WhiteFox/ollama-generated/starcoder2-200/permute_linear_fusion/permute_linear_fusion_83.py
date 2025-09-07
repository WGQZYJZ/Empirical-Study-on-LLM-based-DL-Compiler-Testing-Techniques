
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):

        v3 = input_tensor
        v4 = torch.nn.functional.linear(v3, weight_3, bias=None) # This is a new line added!
        return v4

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 5)


