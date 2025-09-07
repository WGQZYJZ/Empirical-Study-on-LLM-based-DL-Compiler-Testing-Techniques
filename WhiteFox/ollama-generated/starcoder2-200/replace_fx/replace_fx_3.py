
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x):
        return self.linear(x).squeeze(-1), self.linear(x).squeeze(-1), \
               torch.nn.functional.dropout(x), torch.nn.functional.dropout(x)


# Initializing the model
m = Model()


# Inputs to the model
inputs  = [torch.randn(2)]

__output__,  __output_1__, __output_2__, __output_3__ = m(*inputs)


