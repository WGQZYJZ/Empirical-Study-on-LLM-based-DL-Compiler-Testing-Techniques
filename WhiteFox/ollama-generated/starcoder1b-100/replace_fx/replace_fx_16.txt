
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.dropout(x1, self.training) # Dropout only happens at train time.
        return torch.rand_like(t1, 0.) # Fill the original tensor with zeros


# Initializing the model
m = Model()
# ... Run this line for several times to make sure that no optimization takes place here!
x1 = torch.randn(1, 2, 2)
