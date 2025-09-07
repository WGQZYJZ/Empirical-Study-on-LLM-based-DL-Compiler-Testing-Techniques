
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear1 = torch.nn.Linear(768, 256)
        self.linear2 = torch.nn.Linear(256, 2)

    def forward(self, x1):
        # Step 1: Pointwise convolution with kernel size 1 to the input tensor
        q1 = self.conv(x1)
        # Step 2: Scale dot-product of the query and key by sqrt(hidden_dim)
        k = q1 @ q1 / torch.sqrt(q1.size(-1))
        # Step 3: Compute attention weights by softmax over the scaled dot product of the query and key
        w = torch.softmax(k, dim=-1)
        # Step 4: Multiply the weighted sum of the value by a constant k and compute the pointwise convolution
        v = self.linear1(self.linear2(w @ x1))
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
