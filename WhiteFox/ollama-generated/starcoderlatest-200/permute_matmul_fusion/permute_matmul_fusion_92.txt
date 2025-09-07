
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm_layer = torch.nn.BMM()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A to permute the resultant tensor of BMM operation and transpose the last two dimensions
        t1 = torch.bmm(v1, x2) # or torch.matmul(t1, t2)
        return t1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 2, 2)
