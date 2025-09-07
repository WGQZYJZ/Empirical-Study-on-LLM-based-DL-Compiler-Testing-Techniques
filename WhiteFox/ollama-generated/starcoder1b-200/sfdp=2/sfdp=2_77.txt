
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v1_scaled = v1.div(0.7071067811865476)
        v1_softmax = v1_scaled.softmax(-1)  # Apply softmax to the scaled dot product
        v1_dropout = torch.nn.functional.dropout(v1_softmax, p=0.5)
        v2 = x1 * 0.7071067811865476
        return v1_dropout.matmul(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
