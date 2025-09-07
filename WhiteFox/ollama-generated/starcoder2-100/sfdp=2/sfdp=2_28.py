
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        # Initialize the model to be used
        self.__scale_factor__ = 32

        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 / 5000000.0
        v3  = scaled_qk.softmax(dim=-1)
        v4  = dropout_qk.matmul(value)

        return v4


# Inputs to the model
query  = torch.randn(8, 2, 64)
key    = torch.randn(8, 2, 64)
value  = torch.randn(8, 20, 64)

x1 = torch.randn(1, 3, 57, 57)

