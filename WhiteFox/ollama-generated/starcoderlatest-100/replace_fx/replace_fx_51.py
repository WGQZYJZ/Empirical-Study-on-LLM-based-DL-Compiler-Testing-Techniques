
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5) # Dropout in the original graph
        t1 = torch.rand_like(v1, 1e-3) # Generate a tensor with the same size as v1 filled with random numbers
        t2 = x1 * t1 # The replacement is not triggered by the following two lines, because fallback_random=True
        return v1
