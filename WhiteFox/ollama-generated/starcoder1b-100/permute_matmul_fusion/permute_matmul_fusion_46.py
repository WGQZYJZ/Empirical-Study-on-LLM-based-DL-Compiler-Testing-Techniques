
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):
        t1  = x1.permute(0, 2, 1) # Permute the input tensor A or B
        t3  = torch.bmm(t1, x2.permute(0, 2, 1))  # or torch.matmul(t1, x2.permute(0, 2, 1))
        return t3

# Initializing the model
m = Model()


