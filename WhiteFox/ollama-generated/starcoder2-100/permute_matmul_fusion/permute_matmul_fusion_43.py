
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = x1.permute(-1, -3)  # Swapping the last two dimensions of input tensor A
        t2 = x2.permute(-3, -1) # Swapping the last two dimensions of input tensor B 
        v1 = torch.bmm(t1, t2)   # or torch.matmul(t1, t2)
        return v1


# Initializing the model