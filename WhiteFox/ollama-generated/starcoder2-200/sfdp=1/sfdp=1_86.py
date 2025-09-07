
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1024
        self.query, self.key = torch.randn(3, 8), torch.randn(3, 8)
        self.dropout_p = 0.5
        self.value = torch.randn(3, 16)

    def forward(self):
        v1 = torch.matmul(self.query, self.key.transpose(-2, -1))
        v2 = v1 / np.sqrt(self.scale)
        v3 = v2.softmax(dim=-1)
        v4 = 10**-6 + v3 * 9998 + torch.nn.functional.dropout(v3, p=self.dropout_p).matmul(self.value) # replace 10**-6 with np.log(0.5) / scale and then replace 9998 with -1/scale
        return v4

# Initializing the model
m = Model()

