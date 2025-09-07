
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(...) # Permute the input tensor A and then permute it again to produce B.
        t2 = x2.permute(...).permute(...) # Apply permute on both tensors to produce AB or AB^T respectively.
        v1 = self.linear1(t1)
        v2 = self.linear2(v1 + t2)
        return v2
# Initializing the model
m = Model()

