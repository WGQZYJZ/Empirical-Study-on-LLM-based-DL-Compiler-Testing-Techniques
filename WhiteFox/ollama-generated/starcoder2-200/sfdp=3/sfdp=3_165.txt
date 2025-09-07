
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(8, 16)
        self.k = torch.nn.Linear(4, 32)
        self.v = torch.nn.Linear(7, 512)
 
    def forward(self, x):
        v1  = self.q(x) # Compute the dot product of the query tensor and a linear layer output
        v2  = v1 * scale_factor
        v3  = v2 + dropout_p
        v4  = torch.nn.functional.softmax(v3, dim=-1)
        v5  = self.k(x).transpose(-2, -1) # Compute the dot product of the key tensor and a linear layer output transposed on its last two dimensions
        v6  = v4 @ v5
        v7  = torch.nn.functional.dropout(v6, p=dropout_p)
        return self.v(v7)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 8) # random input tensor with size [batch x channels]
__output__  = m(x1)

