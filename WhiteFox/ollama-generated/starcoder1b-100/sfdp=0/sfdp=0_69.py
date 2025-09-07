
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(128, 64)
        self.k = torch.nn.Linear(3, 3)
        self.v = torch.nn.Linear(3, 3)

    def forward(self, x):
        scale_key = self.k(x)
        dot_product_attention = (torch.matmul(scale_key, self.q(x)).softmax(-2) * self.v(x)) / math.sqrt(self.k(x).size(-1))
        return dot_product_attention


# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(1, 64, 3)
key = torch.randn(1, 3, 3)
value = torch.randn(1, 3, 3)
