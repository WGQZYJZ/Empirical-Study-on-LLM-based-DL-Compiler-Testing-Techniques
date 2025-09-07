
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(4096, 768)
        self.k = torch.nn.Linear(4096, 768)
        self.v = torch.nn.Linear(4096, 768)

    def forward(self, x):
        v1  = self.q(x).transpose(-2,-1) # Compute the dot product of the query and key
        v2 = (v1/inv_scale_factor).softmax(dim=-1) # Apply softmax to the scaled dot product

        output = v2.matmul(self.v) # Compute the dot product of the dropout output and a value

        return output
