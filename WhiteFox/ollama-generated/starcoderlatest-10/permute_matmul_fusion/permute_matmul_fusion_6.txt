
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1) # Permute the input tensor A
        t2 = x2.permute(0, 2, 1) # Permute the input tensor B
        