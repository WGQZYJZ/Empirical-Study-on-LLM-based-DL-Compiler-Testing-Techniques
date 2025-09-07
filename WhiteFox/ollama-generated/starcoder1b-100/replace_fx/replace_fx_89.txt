
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, training=True)
        v2 = torch.nn.functional.relu(torch.randn_like(x1, ...))
        v3 = torch.nn.functional.softmax(v2, dim=-1)  # Softmax on the permuted tensor

        return v3


# Initializing the model
m = Model()


