
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.5):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout_p)

        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        # Concatenate tensors along a dimension
        t1 = x1 + x2
        v1 = self.dropout(t1)
        v2 = torch.relu(v1)

        return v2


# Initializing the model
m = Model()

