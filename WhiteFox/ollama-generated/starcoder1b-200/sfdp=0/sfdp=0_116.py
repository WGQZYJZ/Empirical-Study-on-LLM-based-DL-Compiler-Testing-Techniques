
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        query = self.conv(x1)
        key = torch.randn(query.size())
        value = torch.randn(key.size())
        inv_scale = torch.sqrt(torch.mean(query ** 2))  # The square root of the dimension of `key` and `value` helps to stabilize the gradients especially when the dimensions are large
        attention_weights = (query * key).softmax(-1) / inv_scale
        output = attention_weights * value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
