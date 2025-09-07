
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Please remove this node by adding a forward call here:
        v1 = input_tensor.permute(...)
        v2 = torch.nn.functional.dropout(...)

        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
