
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return x1.permute(0, 2, 1).lowmem_dropout(
            torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias), dropout_rate=0.5
        )


# Initializing the model
m = Model()
