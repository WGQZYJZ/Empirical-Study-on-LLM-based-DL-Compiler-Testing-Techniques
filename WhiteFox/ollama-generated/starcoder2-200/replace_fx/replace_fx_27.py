
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, p=0.5) # Apply dropout to the input tensor
        v2 = self.linear(t1)
        return v2

# Initializing the model
m  = Model()

