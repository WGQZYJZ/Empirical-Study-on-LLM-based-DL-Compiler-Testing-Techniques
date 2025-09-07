
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(0, 3, 2) # Permute the input tensor A
        t2 = x2.permute(0, 4, 3) # Permute the input tensor B

        t3_1 = torch.bmm(t1, t2) # torch.matmul or torch.bmm(t1, t2)
        v3   = torch.softmax(t3_1, dim=0)
        return v3


# Initializing the model
m  = Model()


