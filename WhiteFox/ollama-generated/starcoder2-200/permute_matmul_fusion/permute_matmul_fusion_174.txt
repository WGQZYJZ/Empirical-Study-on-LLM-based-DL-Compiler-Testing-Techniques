
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 3, 4) # Permute the input tensor A (2, n, 5, 7) -> (n, 2, 5, 7) 
        v2 = torch.bmm(v1, self.linear_a.weight), bias = self.linear_a.bias,
        v3  = x2.permute(0, 3, 4) # Permute the input tensor B (2, n, 5, 7) -> (n, 2, 5, 7) 
        v4  = torch.bmm(v3, self.linear_b.weight), bias = self.linear_b.bias
        return v1, v2


# Initializing the model: 