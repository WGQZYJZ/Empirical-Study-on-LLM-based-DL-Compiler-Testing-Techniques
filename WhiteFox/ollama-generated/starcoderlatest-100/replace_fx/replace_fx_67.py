
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5) # apply dropout to the input tensor 
        return self.linear(t1)

# Inputs to the model
x1 = torch.randn(2, 16, 4, requires_grad=True)


m = Model()
