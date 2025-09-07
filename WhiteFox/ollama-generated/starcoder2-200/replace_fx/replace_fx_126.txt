

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Replace the dropout nodes with the corresponding replacements when running on CPU devices or when the fallback random config is set
        return torch.nn.functional.dropout(x1, ...)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.rand(2)
__output__  = m(x1)
